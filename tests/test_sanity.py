"""Basic tests to make sure everything works."""

import playground


def test_math():
    """Math still works."""
    assert 2 + 2 == 4


def test_import_playground():
    """Can import the playground package."""
    assert hasattr(playground, "timer")
    assert hasattr(playground, "describe_env")


def test_timer_works():
    """Timer function works correctly."""
    with playground.timer("test") as t:
        sum(range(100))
    
    assert t.seconds >= 0
    assert t.label == "test"


def test_describe_env_works():
    """Environment description works."""
    env = playground.describe_env()
    
    assert "python" in env
    assert "platform" in env
    assert len(env["python"]) > 0
