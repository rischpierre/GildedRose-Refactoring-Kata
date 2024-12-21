# -*- coding: utf-8 -*-
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    """
    Manages the quality and sell in of items inside the Gilded Rose shop
    """

    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items

    def _update_default_item(self, item: Item):
        """
        Once the sell by date has passed, Quality degrades twice as fast
        The Quality of an item is never negative
        The Quality of an item is never more than 50
        """
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality -= 2
        else:
            item.quality -= 1

        item.quality = min(item.quality, self.MAX_QUALITY)
        item.quality = max(item.quality, self.MIN_QUALITY)

    def _update_aged_brie_item(self, item: Item):
        """
        Aged Brie actually increases in Quality the older it gets
        """

        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality += 2
        else:
            item.quality += 1

        item.quality = min(item.quality, self.MAX_QUALITY)

    def _update_sulfuras_item(self, item: Item):
        """
        Sulfuras being a legendary item, never has to be sold or decreases in Quality
        Its Quality is 80 and it never alters
        """
        item.quality = 80

    def _udpate_backstage_item(self, item: Item):
        """
        Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but quality drops to 0 after the concert
        """
        item.sell_in -= 1

        if item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1

        item.quality = min(item.quality, self.MAX_QUALITY)

        if item.sell_in < 0:
            item.quality = 0

    def _update_conjured_item(self, item: Item):
        """
        Conjured items degrade in Quality twice as fast as normal items
        """
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality -= 4
        else:
            item.quality -= 2

        item.quality = max(item.quality, self.MIN_QUALITY)

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self._update_aged_brie_item(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._udpate_backstage_item(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self._update_sulfuras_item(item)
            elif item.name == "Conjured":
                self._update_conjured_item(item)
            else:
                self._update_default_item(item)
