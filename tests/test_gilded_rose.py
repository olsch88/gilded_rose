import pytest
from hypothesis import given
from hypothesis.strategies import text


from ..gilded_rose import Item, GildedRose


@given(text())
def test_no_name_change(sample_name):
    items = [Item(sample_name, 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert sample_name == items[0].name


def test_quality_decreases_default():
    items = [Item("foo", sell_in=5, quality=5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 4


# if __name__ == "__main__":
#     unittest.main()
