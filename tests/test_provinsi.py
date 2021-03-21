from covid19_id import get_prov
from covid19_id.provinsi import DataProvinsi


def test_get_prov():
    prov = get_prov()
    assert isinstance(prov, DataProvinsi)
