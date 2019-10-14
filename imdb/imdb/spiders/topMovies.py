# -*- coding: utf-8 -*-
import scrapy


class TopmoviesSpider(scrapy.Spider):
    name = 'topMovies'
    allowed_domains = ['https://www.imdb.com/chart/top']
    start_urls = ['http://https://www.imdb.com/chart/top/']

    def parse(self, response):
        pass
