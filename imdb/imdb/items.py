# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    genre = scrapy.Field()
    contentRating = scrapy.Field()
    actor = scrapy.Field()
    creator = scrapy.Field()
    description = scrapy.Field()
    datePublished = scrapy.Field()
    keywords = scrapy.Field()
    aggregateRating = scrapy.Field()
    review = scrapy.Field()
    trailer = scrapy.Field()
    duration = scrapy.Field()
    pass
