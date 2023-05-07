from queue import Queue
import time
import threading

__version__ = "0.1.0"
__author__ = 'Sajeeb Lohani'


class RateLimitQueue:
    def __init__(self, num_calls, secs=0, mins=0, hours=0):
        self.time_period = secs + (mins * 60) + (hours * 3600)
        self.num_calls = num_calls
        self.queue = Queue()
        self.call_times = list()
        self.lock = threading.Lock()

    def put(self, item):
        self.queue.put(item)

    def put_list(self, item_list):
        for item in item_list:
            self.queue.put(item)

    def _clean_call_times(self, oldest_time):
        return [t for t in self.call_times if t >= oldest_time]

    def _update_times(self):
        self.current_time = time.monotonic()
        self.oldest_time = self.current_time - self.time_period

    def get(self):
        if len(self.queue) == 0:
            raise EmptyRateLimitQueue("The rate limit queue is empty", "RLQ-1")
        self._update_times()

        with self.lock:
            self.call_times = self._clean_call_times(self.oldest_time)

            while len(self.call_times) >= self.num_calls:
                time_to_wait = self.call_times[0] + self.time_period - self.current_time
                if time_to_wait > 0:
                    time.sleep(time_to_wait)
                self._update_times()
                self.call_times = self._clean_call_times(self.oldest_time)

            item = self.queue.get()
            self.call_times.append(self.current_time)
            return item


class EmptyRateLimitQueue(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code
