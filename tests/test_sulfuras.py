from hypothesis import given
from hypothesis.strategies import text, integers

from ..gilded_rose import Item, GildedRose


def test_quality_sulfuras():
    items = [Item("Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80


@given(start_sell_in=integers(min_value=-10, max_value=10))
def test_sell_in_sulfuras(start_sell_in):
    items = [Item("Sulfuras, Hand of Ragnaros", sell_in=start_sell_in, quality=5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == start_sell_in
