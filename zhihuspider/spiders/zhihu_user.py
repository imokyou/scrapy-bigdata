# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request, FormRequest
from scrapy.linkextractors import LinkExtractor
from zhihuspider.items import ZhihuUserspiderItem
import urlparse
from zhihuspider.settings import *


class ZhihuUserSpider(CrawlSpider):
    name = "zhihu_user"
    host = "http://www.zhihu.com"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
        'http://www.zhihu.com/people/alex-an'
    ]
    rules = [
        Rule(LinkExtractor(allow=("http://www\.zhihu\.com/people/[0-9a-zA-Z]+/about", )), callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=("http://www\.zhihu\.com/people/[0-9a-zA-Z]+", )), callback='parse_item',follow=True),
    ]

    def __init__(self,  *a,  **kwargs):
        super(ZhihuUserSpider, self).__init__(*a, **kwargs)

    def start_requests(self):
        return [FormRequest(
            "http://www.zhihu.com/login/email",
            formdata = {'email':'1026703049@qq.com',
                        'password':'lu7457267293'
            },
            callback = self.after_login
        )]

    def after_login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse_item(self, response):
        params = urlparse.urlparse(response.url)
        selector = Selector(response)
        for link in selector.xpath('//div[@class="zm-item-answer-author-info"]/h3/a/@href').extract():
            if link != params.path:
                yield Request(self.host+link, callback=self.parse_user)

    def parse_user(self, response):
        result = urlparse.urlparse(response.url)
        item = ZhihuUserspiderItem()
        sex = response.css('.zm-rich-follow-btn').xpath('text()').extract()[0]
        account = result.path.split('/')[2]
        nickname = response.css('.ellipsis').xpath('./a/text()').extract()
        if not nickname:
            nickname = response.css('.ellipsis').xpath('./span/text()').extract()

        item['url'] = response.url
        item['account'] = account
        item['nickname'] = nickname[0].strip()
        item['location'] = ' '.join(response.css('.location').xpath('text()').extract())
        item['industry'] = ' '.join(response.css('.business').xpath('./a/text()').extract())
        item['sex'] = sex
        # item['achievement'] = response.css('.zm-profile-module-desc').xpath('./span/strong/text()').extract()
        item['achievement'] = []
        item['asks'] = response.xpath('//a[contains(@href, "/people/'+account+'/asks")]/span/text()').extract()[0]
        item['answers'] = response.xpath('//a[contains(@href, "/people/'+account+'/answers")]/span/text()').extract()[0]
        item['followees'] = response.xpath('//a[contains(@href, "/people/'+account+'/followees")]/strong/text()').extract()[0]
        item['followers'] = response.xpath('//a[contains(@href, "/people/'+account+'/followers")]/strong/text()').extract()[0]
        yield item
