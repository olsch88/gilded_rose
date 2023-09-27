# -*- coding: utf-8 -*-

from enum import StrEnum, auto


class Articles(StrEnum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    CONJURED = "Conjured Mana Cake"


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


def update__default(item: Item) -> None:
    item.sell_in = item.sell_in - 1
    decrease_quality(item)
    if item.sell_in < 0:
        decrease_quality(item)


def update_brie(item: Item) -> None:
    item.sell_in = item.sell_in - 1
    increase_quality(item)


def update_backstage(item: Item) -> None:
    item.sell_in = item.sell_in - 1
    increase_quality(item)
    if item.sell_in < 10:
        increase_quality(item)
    if item.sell_in < 5:
        increase_quality(item)
    if item.sell_in < 0:
        item.quality = 0


def update_conjured(item) -> None:
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        decrease_quality(item, amount=4)
    else:
        decrease_quality(item, amount=2)


def update_sulfuras(item: Item) -> None:
    pass


update_functions = {
    Articles.AGED_BRIE: update_brie,
    Articles.SULFURAS: update_sulfuras,
    Articles.BACKSTAGE_PASS: update_backstage,
    Articles.CONJURED: update_conjured,
}


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_func = update_functions.get(item.name, update__default)
            update_func(item)
