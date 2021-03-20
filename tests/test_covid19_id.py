from covid19_id import __version__, get_update, UpdateCovid19


def test_version():
    assert __version__ == "0.2.0"


def test_update_covid19():
    update = get_update()
    assert isinstance(update, UpdateCovid19)
