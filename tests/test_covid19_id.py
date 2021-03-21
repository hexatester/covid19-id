from covid19_id import (
    __version__,
    get_update,
    get_prov,
    get_pemeriksaan_vaksinasi,
    UpdateCovid19,
    DataProvinsi,
    PemeriksaanVaksinasi,
)


def test_version():
    assert __version__ == "0.4.0"


def test_update_covid19():
    update = get_update()
    assert isinstance(update, UpdateCovid19)


def test_get_prov():
    prov = get_prov()
    assert isinstance(prov, DataProvinsi)


def test_pemeriksaan_vaksinasi():
    pemeriksaan_vaksinasi = get_pemeriksaan_vaksinasi()
    assert isinstance(pemeriksaan_vaksinasi, PemeriksaanVaksinasi)
