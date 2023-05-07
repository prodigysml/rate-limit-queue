from rate_limit_queue import RateLimitQueue, EmptyRateLimitQueue
import time
import pytest


def test_rate_limit_queue_creation():
    r = RateLimitQueue(10, secs=10)
    assert isinstance(r, RateLimitQueue)
    assert r.num_calls == 10
    assert r.time_period == 10


def test_time_period():
    r = RateLimitQueue(10, secs=10)
    assert r.time_period == 10
    r = RateLimitQueue(10, secs=10, mins=10)
    assert r.time_period == 610
    r = RateLimitQueue(10, secs=10, hours=10)
    assert r.time_period == 36010


def test_put_items():
    r = RateLimitQueue(3, secs=1)
    r.put("test1")
    r.put("test2")
    r.put("test3")

    for i in range(1, 4):
        assert r.get() == f"test{i}"

    range_list = list(range(10))

    r.put_list(range_list)

    for i in range(3):
        assert r.get() == i


def test_get_items():
    r = RateLimitQueue(3, secs=3)
    r.put_list(list(range(5)))

    start_time = time.time()
    for _ in range(5):
        r.get()

    assert 3 < time.time() - start_time < 4


def test_empty_queue():
    r = RateLimitQueue(3, secs=3)
    with pytest.raises(EmptyRateLimitQueue):
        r.get()
