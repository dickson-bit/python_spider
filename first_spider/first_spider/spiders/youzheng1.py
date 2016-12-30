# -*- coding: utf-8 -*-
import scrapy


class Youzheng1Spider(scrapy.Spider):
    name = "youzheng1"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        pass
