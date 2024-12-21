# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_if_sell_date_passed_then_quality_degrades_twice_as_fast(self):
        item = Item("test", 1, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        # init quality -> 10
        # -1 for the first iteration
        # -2 for the second
        # so 10 -3 for the end quality
        self.assertEqual(item.quality, 7)

    def test_quality_never_negative(self):
        item = Item("test", 1, 1)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)

    def test_aged_brie_quality_increases_the_older_it_gets(self):
        item = Item("Aged Brie", 1, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 13)

    def test_max_50_quality(self):
        item = Item("Aged Brie", 1, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)

    def test_sulfuras_never_sold_or_loose_quality(self):
        item = Item("Sulfuras, Hand of Ragnaros", 1, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 50)
        self.assertEqual(item.sell_in, 1)

    def test_backstage_quality_rate_increase_by_2_with_10_days_or_less(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 6)
        self.assertEqual(item.quality, 34)

    def test_backstage_quality_rate_increase_by_3_when_with_5_days_or_less(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 36)
        self.assertEqual(item.sell_in, 3)

    def test_backstage_quality_drops_to_0_after_the_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 30)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.quality, 0)

    def test_conjured_degrate_in_quality_twice_as_fast_as_normal_items(self):
        init_quality = 5
        normal_item = Item("test", 5, init_quality)
        gilded_rose = GildedRose([normal_item])
        gilded_rose.update_quality()

        conjured_item = Item("Conjured", 5, init_quality)
        gilded_rose = GildedRose([conjured_item])
        gilded_rose.update_quality()
        self.assertEqual(
            (init_quality - normal_item.quality) * 2,
            init_quality - conjured_item.quality,
        )


if __name__ == "__main__":
    unittest.main()
