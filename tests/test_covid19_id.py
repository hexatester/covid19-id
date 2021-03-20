from covid19_id import __version__, get_update, get_prov, UpdateCovid19, DataProvinsi


def test_version():
    assert __version__ == "0.3.0"


def test_update_covid19():
    update = get_update()
    assert isinstance(update, UpdateCovid19)


def test_get_prov():
    prov = get_prov()
    assert isinstance(prov, DataProvinsi)
