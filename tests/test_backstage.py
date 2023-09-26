from hypothesis import given
from hypothesis.strategies import text, integers

from ..gilded_rose import Item, GildedRose


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_backstage_long_time(start_quality):
    items = [
        Item(
            "Backstage passes to a TAFKAL80ETC concert",
            sell_in=11,
            quality=start_quality,
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == min(50, start_quality + 1)


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_backstage_medium_time(start_quality):
    items = [
        Item(
            "Backstage passes to a TAFKAL80ETC concert",
            sell_in=8,
            quality=start_quality,
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == min(50, start_quality + 2)


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_backstage_short_time(start_quality):
    items = [
        Item(
            "Backstage passes to a TAFKAL80ETC concert",
            sell_in=3,
            quality=start_quality,
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == min(50, start_quality + 3)


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_backstage_no_time(start_quality):
    items = [
        Item(
            "Backstage passes to a TAFKAL80ETC concert",
            sell_in=0,
            quality=start_quality,
        )
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0
