# covid19-id

[![covid19-id - PyPi](https://img.shields.io/pypi/v/covid19-id)](https://pypi.org/project/covid19-id/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/covid19-id)](https://pypi.org/project/covid19-id/)
[![LICENSE](https://img.shields.io/github/license/hexatester/covid19-id)](https://github.com/hexatester/covid19-id/blob/main/LICENSE)
[![codecov](https://codecov.io/gh/hexatester/covid19-id/branch/main/graph/badge.svg)](https://codecov.io/gh/hexatester/covid19-id)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Mypy](https://img.shields.io/badge/Mypy-enabled-brightgreen)](https://github.com/python/mypy)

Modul python untuk mengambil data dari covid19.go.id

## Install

Anda dapat menginstall atau mengupdate covid19-id dengan perintah:

```bash
pip install covid19-id --upgrade
```

## Dependensi Tambahan

covid19-id dapat diinstall dengan modul tambahan [ujson](https://pypi.org/project/ujson/ "ujson - PyPi").

```bash
pip install covid19-id[ujson]
```

Modul `ujson` tersebut akan digunakan untuk mendekode JSON, yang lebih cepat dibandingkan dengan standard [json](https://docs.python.org/3/library/json.html "python json docs") modul.

## Contoh

### Mendapat Pembaruan

```python
import covid19_id

all_update = covid19_id.get_update()

total = all_update.update.total

print(f"covid19; kasus positif di Indonesia : {total.jumlah_positif}")
print(f"covid19; pasien dirawat di Indonesia {total.jumlah_dirawat}")
print(f"covid19; pasien sembuh di Indonesia {total.jumlah_sembuh}")
print(f"covid19; pasien meninggal Indonesia {total.jumlah_meninggal}")

```

### Data Provinsi

```python
import covid19_id

data_provinsi = covid19_id.get_prov()

for provinsi in data_provinsi.list_data:
    print(f"Nama Provinsi : {provinsi.key}")
    print(f"Jumlah Kasus {provinsi.jumlah_kasus}")
    print(f"Jumlah Sembuh {provinsi.jumlah_sembuh}")
    print(f"Jumlah Meninggal {provinsi.jumlah_meninggal}")
    for umur in provinsi.kelompok_umur:
        print(f"Umur {umur.key} : {umur.doc_count}")
    penambahan = provinsi.penambahan
    print(f"Kasus Positif tambahan {penambahan.positif}")
    print(f"Tambahan sembuh {penambahan.sembuh}")
    print(f"Tambahan meninggal {penambahan.meninggal}")
    print("")

```

### Pemeriksaan dan Vaksinasi

```python
import covid19_id


pemeriksaan_vaksinasi = covid19_id.get_pemeriksaan_vaksinasi()

vaksinasi_total = pemeriksaan_vaksinasi.vaksinasi.total

print(f"Jumlah vaksinasi pertama {vaksinasi_total.jumlah_vaksinasi_1}")
print(f"Jumlah vaksinasi kedua {vaksinasi_total.jumlah_vaksinasi_2}")

```
