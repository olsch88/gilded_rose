# -*- coding: utf-8 -*-

from enum import StrEnum, auto


class Articles(StrEnum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


def increase_quality(item: Item, amount: int = 1, max_value=50) -> None:
    item.quality = min(item.quality + amount, 50)


def decrease_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(item.quality - amount, 0)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != Articles.SULFURAS:
                item.sell_in = item.sell_in - 1

            if item.name != Articles.AGED_BRIE and item.name != Articles.BACKSTAGE_PASS:
                if item.name != Articles.SULFURAS:
                    decrease_quality(item)
            else:
                increase_quality(item)
                if item.name == Articles.BACKSTAGE_PASS:
                    if item.sell_in < 10:
                        increase_quality(item)
                    if item.sell_in < 5:
                        increase_quality(item)

            if item.sell_in < 0:
                if item.name == Articles.SULFURAS:
                    pass
                elif item.name == Articles.BACKSTAGE_PASS:
                    item.quality = 0
                elif item.name == Articles.AGED_BRIE:
                    increase_quality(item)

                else:
                    decrease_quality(item)
