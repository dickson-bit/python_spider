# -*- coding: utf-8 -*-
import scrapy


class Youzheng2Spider(scrapy.Spider):
    name = "youzheng2"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        pass
