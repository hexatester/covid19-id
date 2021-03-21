from covid19_id import get_pemeriksaan_vaksinasi
from covid19_id.pemeriksaan_vaksinasi import PemeriksaanVaksinasi


def test_pemeriksaan_vaksinasi():
    pemeriksaan_vaksinasi = get_pemeriksaan_vaksinasi()
    assert isinstance(pemeriksaan_vaksinasi, PemeriksaanVaksinasi)
