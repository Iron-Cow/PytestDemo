def test_a1():
    assert 4 >= 3


def test_a2():
    assert 1  # assert bool(1)


def test_a3():
    assert 1 in divmod(9, 5)
    ev, r = divmod(9, 5)
    assert ev == 1
    assert r == 4


