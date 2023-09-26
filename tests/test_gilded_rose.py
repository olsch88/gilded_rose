import pytest
from hypothesis import given
from hypothesis.strategies import text, integers


from ..gilded_rose import Item, GildedRose


@given(text())
def test_no_name_change(sample_name):
    items = [Item(sample_name, 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert sample_name == items[0].name


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_decreases_default(start_quality):
    items = [Item("foo", sell_in=5, quality=start_quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == max(0, start_quality - 1)


@given(start_quality=integers(min_value=1, max_value=50))
def test_quality_decreases_after_date(start_quality):
    items = [Item("foo", sell_in=-1, quality=start_quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == max(0, start_quality - 2)


@given(start_sell_in=integers(min_value=1))
def test_sell_in_decreases_default(start_sell_in):
    items = [Item("foo", sell_in=start_sell_in, quality=5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == start_sell_in - 1
