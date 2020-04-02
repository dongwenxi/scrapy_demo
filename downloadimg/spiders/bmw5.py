# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_test.downloadimg.downloadimg.items import DownloadimgItem


class Bmw5Spider(CrawlSpider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'),
             callback='parse_page', follow=True), )

    def parse_page(self, response):
        # selectorlist -> list
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
                # url = 'https:' + url
                # url = response.urljoin(url)
            urls = list(map(lambda url: response.urljoin(url), urls))
            urls = list(map(lambda url: url.replace('t_', ''), urls))
            item = DownloadimgItem(category=category, image_urls=urls)
            yield item


    def test_parse(self):
        pass