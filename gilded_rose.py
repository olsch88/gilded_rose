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


def increase_quality(item: Item) -> None:
    pass


def decrease_quality(item: Item) -> None:
    pass


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != Articles.AGED_BRIE and item.name != Articles.BACKSTAGE_PASS:
                if item.quality > 0:
                    if item.name != Articles.SULFURAS:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == Articles.BACKSTAGE_PASS:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != Articles.SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != Articles.AGED_BRIE:
                    if item.name != Articles.BACKSTAGE_PASS:
                        if item.quality > 0:
                            if item.name != Articles.SULFURAS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
