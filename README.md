# Rate Limit Queue

An implementation of rate limited queues in Python, thread-safe, using only built-in components. 

**Note: The rate limit only applies on retrieval from the queue, not placing inside the queue.**

# Unit Tests

Unit tests are performed using `pytest`. Install `pytest` using `pip`.

# Coding Guidelines

This project is being maintained using the PEP8 standard. We are using `flake8` to ensure the standard is upheld.

# Usage

## Instantiation of the Queue
Instantiating a `RateLimitQueue` object requires at least 1 parameter. Below is a list of all the compatible parameters:

| Parameter Name | Type  | Usage                                                        | Required? |
|----------------|-------|--------------------------------------------------------------|-----------|
| `num_calls`    | `int` | The number of calls to make, per time period (e.g. 10 / 30s) | Yes       |
| `secs`         | `int` | The number of seconds in the time period (e.g. 90s)          | No        |
| `mins`         | `int` | The number of minutes in the time period (e.g. 90 minutes)   | No        |
| `hours`        | `int` | The number of hours in the time period (e.g. 48 hours)       | No        |

The time period is adjustable and incremental. It was made with flexibility in mind, allowing a user to specify `1.5 mins` as `90 secs`, `1.5 mins`, and `1 mins 30 secs`.

## Getting and Putting into the Queue

### Put

Upon instantiating the queue, simply use either `put()` or `put_list()` to place items in the queue. The queue is not type strict, so any type of object or data structure can be placed within this queue.

```python
from rate_limit_queue import RateLimitQueue

queue_of_my_fav_sites = RateLimitQueue(10, secs=10)

queue_of_my_fav_sites.put("https://github.com")

list_of_my_fav_sites = ["https://bugcrowd.com", "https://example.com", "https://portswigger.net"]

queue_of_my_fav_sites.put_list(list_of_my_fav_sites)
```

### Get

After putting into the queue, retrieval is quite simple. Use the `put` method to retrieve the object in the same way you stored it.

```python
from rate_limit_queue import RateLimitQueue

queue_of_my_fav_sites = RateLimitQueue(10, secs=10)

queue_of_my_fav_sites.put("https://github.com")

print(queue_of_my_fav_sites.get())
```

**Note: Should your queue run out of items, make sure you keep your eyes peeled for the `EmptyRateLimitQueue` exception**

```python
from rate_limit_queue import RateLimitQueue

queue_of_my_fav_sites = RateLimitQueue(10, secs=10)

queue_of_my_fav_sites.put("https://github.com")

print(queue_of_my_fav_sites.get())

queue_of_my_fav_sites.get() # raises EmptyRateLimitQueue
```