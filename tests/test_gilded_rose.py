import pytest

from ..gilded_rose import Item, GildedRose


def test_no_name_change():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


def test_quality_decreases_default():
    items = [Item("foo", sell_in=5, quality=5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 4


# if __name__ == "__main__":
#     unittest.main()
