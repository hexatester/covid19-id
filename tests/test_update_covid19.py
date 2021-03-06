from datetime import datetime

from covid19_id import get_update
from covid19_id.update_covid19 import UpdateCovid19
from covid19_id.update_covid19 import Harian


def test_update_covid19():
    update = get_update()
    assert isinstance(update, UpdateCovid19)
    if update.update.today:
        assert isinstance(update.update.today, Harian)
    for harian in update.update.harian:
        assert isinstance(harian, Harian)
        assert isinstance(harian.datetime, datetime)
        break
