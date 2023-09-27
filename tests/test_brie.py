from hypothesis import given
from hypothesis.strategies import text, integers

from ..gilded_rose import Item, GildedRose


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_brie_increase(start_quality):
    items = [Item("Aged Brie", sell_in=5, quality=start_quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == min(max(0, start_quality + 1), 50)


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_brie_increase_after_date(start_quality):
    items = [Item("Aged Brie", sell_in=-5, quality=start_quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == min(max(0, start_quality + 1), 50)


@given(start_sell_in=integers(min_value=-10, max_value=10))
def test_sell_in_decreases_brie(start_sell_in):
    items = [Item("Aged Brie", sell_in=start_sell_in, quality=5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == start_sell_in - 1
