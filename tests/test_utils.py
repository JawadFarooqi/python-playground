"""Test the utility functions."""

from playground import describe_env, timer


def test_describe_env_has_required_info():
    """Environment info includes what we need."""
    env = describe_env()
    required_keys = ["python", "platform", "executable", "cwd"]
    
    for key in required_keys:
        assert key in env, f"Missing key: {key}"


def test_timer_measures_time():
    """Timer correctly measures time."""
    with timer("test operation") as t:
        # Do some work
        total = sum(range(1000))
    
    assert t.seconds >= 0
    assert "test operation" in str(t)
