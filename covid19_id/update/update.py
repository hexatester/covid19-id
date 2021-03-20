import attr
from typing import List

from . import Data
from . import Penambahan
from . import Harian
from . import Total


@attr.dataclass(slots=True)
class Update:
    data: Data
    penambahan: Penambahan
    harian: List[Harian]
    total: Total
