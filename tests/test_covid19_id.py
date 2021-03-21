from covid19_id import (
    __version__,
    get_prov,
    get_pemeriksaan_vaksinasi,
    DataProvinsi,
    PemeriksaanVaksinasi,
)


def test_version():
    assert __version__ == "0.4.0"


def test_get_prov():
    prov = get_prov()
    assert isinstance(prov, DataProvinsi)


def test_pemeriksaan_vaksinasi():
    pemeriksaan_vaksinasi = get_pemeriksaan_vaksinasi()
    assert isinstance(pemeriksaan_vaksinasi, PemeriksaanVaksinasi)
