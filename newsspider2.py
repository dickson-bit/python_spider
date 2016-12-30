# coding:utf-8
__author__ = 'guodl'

import urllib2
from lxml import etree

def get_seeds():
    urls = ['http://auto.sina.com.cn/newcar/index.d.html']

    return urls
    pass

def get_url_content(url):
    response = urllib2.urlopen(url)

    return response


def get_html_link(response, config=None):
    dom_tree = etree.HTML(response.read())

    result = dom_tree.xpath('//div[@class]//div[contains(@class, "s-left")]//h3/a/@href')

    for item in result:
        yield item

    pass

def get_html_text(response, config=None):
    dom_tree = etree.HTML(response.read())

    result = dom_tree.xpath('//div[@id="articleContent"]/p//text()')
    text = ""

    for item in result:
        text += item

    return text
    pass


if __name__ == "__main__":
    #加载配置

    # 获取种子
    url_list = get_seeds()

    # 带采集队列
    link_list = []

    # 下载链接
    for url in url_list:
        # download
        response = get_url_content(url)

        # parse response link
        link_list = get_html_link(response)

    # 处理二级页面, 获取带采集链接
    for url in link_list:
        # download
        response = get_url_content(url)

        # parse response link
        temp_list = get_html_link(response)

        # parse response text
        text = get_html_text(response)

        # 预处理，

