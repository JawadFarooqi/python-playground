from playground import describe_env, timer


def test_describe_env_keys():
    env = describe_env()
    for key in ["python", "implementation", "platform", "executable", "cwd"]:
        assert key in env


def test_timer_context():
    with timer("quick") as t:
        sum(range(1000))
    assert t.seconds >= 0
