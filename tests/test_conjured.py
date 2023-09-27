from hypothesis import given
from hypothesis.strategies import text, integers

from ..gilded_rose import Item, GildedRose


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_conjured_increase(start_quality):
    items = [Item("Conjured Mana Cake", sell_in=5, quality=start_quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == min(max(0, start_quality - 2), 50)


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_conjured_increase_after_date(start_quality):
    items = [Item("Conjured Mana Cake", sell_in=-2, quality=start_quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == min(max(0, start_quality - 4), 50)
