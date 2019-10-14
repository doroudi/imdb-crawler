# -*- coding: utf-8 -*-
import scrapy


class TopmoviesSpider(scrapy.Spider):
    name = 'topMovies'
    allowed_domains = ['https://www.imdb.com/chart/top']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        titles = response.css(".lister-list .titleColumn a::text").extract()
        for title in titles:
            print(title)
        pass
