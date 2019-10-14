# -*- coding: utf-8 -*-
import scrapy


class TopmoviesSpider(scrapy.Spider):
    name = 'topMovies'
    allowed_domains = ['https://www.imdb.com/chart/top']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        movies = response.css(".lister-list tr")
        for movie in movies:
            yield {
                'image': movie.css('.posterColumn img::attr(src)').extract_first(),
                'title': movie.css('.titleColumn a::text').extract_first(),
                'link': movie.css('.titleColumn a::text').extract_first(),
                'rate': movie.css('.ratingColumn strong::text').extract_first()
            }
            pass
