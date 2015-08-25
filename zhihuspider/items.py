# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuspiderItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    location = scrapy.Field()


class ZhihuQspiderItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    question_id = scrapy.Field()
    question_title = scrapy.Field()
    answer_nums = scrapy.Field()


class DoubanGspiderItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    group_id = scrapy.Field()
    group_name = scrapy.Field()
    group_tags = scrapy.Field()
    menbership = scrapy.Field()
    create_time = scrapy.Field()
    chef = scrapy.Field()


class ZhihuUserspiderItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field()
    account = scrapy.Field()
    nickname = scrapy.Field()
    location = scrapy.Field()
    industry = scrapy.Field()
    sex = scrapy.Field()
    achievement = scrapy.Field()
    asks = scrapy.Field()
    answers = scrapy.Field()
    followees = scrapy.Field()
    followers = scrapy.Field()
