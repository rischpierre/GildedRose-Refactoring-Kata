# -*- coding: utf-8 -*-
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items

    def update_default(self, item: Item):
        if item.quality > self.MIN_QUALITY:
            item.quality -= 1

        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

    def update_aged_brie(self, item: Item):
        if item.quality < self.MAX_QUALITY:
            item.quality += 1

        item.sell_in -= 1

        if item.sell_in < 0 and item.quality < self.MAX_QUALITY:
            item.quality += 1

    def update_sulfuras(self, item: Item):
        # there is nothing to do on sulfuras
        pass

    def udpate_backstage(self, item: Item):

        item.quality += 1

        if item.sell_in < 11:
            item.quality += 1
        if item.sell_in < 6:
            item.quality += 1

        item.sell_in -= 1
        item.quality = min(item.quality, self.MAX_QUALITY)

        if item.sell_in < 0:
            item.quality = 0

    def update_conjured(self, item: Item):
        if item.quality > self.MIN_QUALITY:
            item.quality -= 2

        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > self.MIN_QUALITY:
            item.quality -= 2

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.udpate_backstage(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.update_sulfuras(item)
            elif item.name == "Conjured":
                self.update_conjured(item)
            else:
                self.update_default(item)
