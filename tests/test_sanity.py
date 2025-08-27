def test_math():
    assert 2 + 2 == 4


def test_import_package():
    import playground
    assert hasattr(playground, "timer")
