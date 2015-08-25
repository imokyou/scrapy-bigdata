# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from zhihuspider.items import DoubanGspiderItem
import urlparse


class ZhihuSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["www.douban.com"]
    start_urls = [
        # 'http://www.douban.com',
        'http://www.douban.com/group/dalirenmin/'
    ]
    rules = [
        Rule(LinkExtractor(allow=("http://www\.douban\.com/group/[0-9a-zA-Z]+/$", )), callback='parse_item',follow=True),
    ]

    def parse_item(self, response):
        # 在这里只获取页面的 URL 以及下载数量
        result = urlparse.urlparse(response.url)
        item = DoubanGspiderItem()

        item['url'] = response.url
        item['group_id'] = result.path.split('/')[2]
        item['group_name'] = response.xpath("//div[@id='group-info']").xpath("./h1/text()").extract()[0].replace('\n','').strip()
        item['group_tags'] = response.css('.group-tags').xpath('./a/text()').extract()
        item['menbership'] = response.css('.side-nav').xpath('./p/a/text()').re(r'\((.*)\)')[0]
        item['create_time'] = response.css('.group-board').xpath('./p/text()').re(r'([0-9\-]+)')[0]
        item['chef'] = response.css('.group-board').xpath('./p/a/text()').extract()[0]
        yield item
