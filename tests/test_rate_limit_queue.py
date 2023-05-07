from rate_limit_queue import RateLimitQueue


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
