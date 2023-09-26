from hypothesis import given
from hypothesis.strategies import text, integers

from ..gilded_rose import Item, GildedRose


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_brie_increase(start_quality):
    items = [Item("Aged Brie", sell_in=0, quality=start_quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == min(max(0, start_quality + 1), 50)
