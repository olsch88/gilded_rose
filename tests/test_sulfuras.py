from hypothesis import given
from hypothesis.strategies import text, integers

from ..gilded_rose import Item, GildedRose


def test_quality_sulfuras():
    items = [Item("Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80
