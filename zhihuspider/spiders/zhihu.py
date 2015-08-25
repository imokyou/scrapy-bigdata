# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from zhihuspider.items import ZhihuQspiderItem
import urlparse


def stripN(items):
    result = []
    for item in items:
        result.append(item.replace('\n',''))
    return result


class ZhihuSpider(CrawlSpider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
        # 'http://www.zhihu.com',
        'http://www.zhihu.com/question/23271398/answer/20451304'
    ]
    rules = [
        Rule(LinkExtractor(allow=("http://www\.zhihu\.com/question/", )), callback='parse_item',follow=True),
    ]

    def parse_item(self, response):
        # 在这里只获取页面的 URL 以及下载数量
        result = urlparse.urlparse(response.url)
        item = ZhihuQspiderItem()

        title = stripN(response.css('.zm-item-title').xpath('./a/text()').extract())
        if not title:
            title = response.css('.zm-item-title').xpath('./text()').extract()

        answer_nums = response.xpath("//h3[@id='zh-question-answer-num']").xpath("text()").re(r'([0-9]+)')
        if not answer_nums:
            answer_nums = response.css('.zg-link-litblue').xpath('./text()').extract().re(r'([0-9]+)')

        item['url'] = response.url
        item['question_id'] = result.path.split('/')[2]
        item['question_title'] = title[0]
        item['answer_nums'] = answer_nums
        yield item
