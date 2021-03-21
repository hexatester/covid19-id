import attr


@attr.dataclass(slots=True)
class PemeriksaanTotal:
    jumlah_spesimen_pcr_tcm: int
    jumlah_spesimen_antigen: int
    jumlah_orang_antigen: int
    jumlah_orang_pcr_tcm: int
