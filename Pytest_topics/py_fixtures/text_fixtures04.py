months = ["J", "F", "M"]


def test_check_request(setup04):
    assert "A" in months
    assert len(months) == 4


def test_factory_fixture(setup05):
    assert type(setup05('list')) == list
    assert type(setup05('tuple')) == tuple
