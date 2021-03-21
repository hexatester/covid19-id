from datetime import date

from covid19_id import get_data
from covid19_id.data import Data
from covid19_id.data import Kasus
from covid19_id.data import Sembuh
from covid19_id.data import Meninggal
from covid19_id.data import Perawatan


def test_get_data():
    data = get_data()
    assert isinstance(data, Data)
    assert isinstance(data.last_update, date)
    assert isinstance(data.kasus, Kasus)
    assert isinstance(data.sembuh, Sembuh)
    assert isinstance(data.meninggal, Meninggal)
    assert isinstance(data.perawatan, Perawatan)
