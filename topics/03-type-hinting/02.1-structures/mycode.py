from typing import TYPE_CHECKING
from pkg import process



pr = process(5)
if TYPE_CHECKING:
    reveal_type(pr)

pr2 = process(bytes("123", encoding="utf8"))
if TYPE_CHECKING:
    reveal_type(pr2)