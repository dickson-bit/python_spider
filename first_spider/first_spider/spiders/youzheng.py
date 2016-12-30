# -*- coding: utf-8 -*-
import scrapy
from first_spider.items import FirstSpiderItem


class YouzhengSpider(scrapy.Spider):
    name = "youzheng"
    start_urls = (
        'http://news.baidu.com/',
    )

    # parse response for link and text
    def parse(self, response):

        links = response.xpath('//div[@id="pane-news"]//a/@href').extract()
        for url in links:
            yield scrapy.Request(url, dont_filter=True)

        item = FirstSpiderItem()

        item['content'] = "test"

        yield item

        pass
