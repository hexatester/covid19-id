import attr


@attr.dataclass(slots=True)
class HarianValue(int):
    value: int

    def __get__(self, instance, owner):
        return self.value


@attr.dataclass(slots=True)
class Harian:
    key_as_string: str
    key: int
    doc_count: int
    jumlah_meninggal: HarianValue
    jumlah_sembuh: HarianValue
    jumlah_positif: HarianValue
    jumlah_dirawat: HarianValue
    jumlah_positif_kum: HarianValue
    jumlah_sembuh_kum: HarianValue
    jumlah_meninggal_kum: HarianValue
    jumlah_dirawat_kum: HarianValue
