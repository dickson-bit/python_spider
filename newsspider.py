# -*- coding: utf-8 -*-
import urllib2
from lxml import etree
import sys
import time

print sys.getdefaultencoding()


def getseed():
    urls = ['http://auto.sina.com.cn/newcar/index.d.html']

    return urls
    pass

def get_url_download(url):

    return urllib2.urlopen(url)
    response = urllib2.urlopen(url)

    if response.getcode() == 200:
        return response

    pass

def parse_html_link(response):
        html = etree.html(response.read())

        # 获取连接信息
        href_list = html.xpath('//div[@class]//div[contains(@class, "s-left")]//h3/a/@href')
        for href in href_list:
            yield href


def parse_html_text(response):
        html = etree.HTML(response.read())
        print response.url

        # 获取文本信息
        items = html.xpath('//div[@id="articleContent"]/p//text()')

        for item in items:
            yield item




if __name__ == "__main__":
    urls = getseed()

    url_list = []

    for url in urls:
        response = get_url_download(url)
        result = parse_html_link(response)

        for item in result:
            url_list.append(item)
            print item

    for item in url_list:
        response = get_url_download(item)
        result = parse_html_text(response)
        print type(result)
        for item in result:
            print item

        time.sleep(1)

