# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from settings import *
from items import ZhihuspiderItem
from items import ZhihuQspiderItem
from items import ZhihuUserspiderItem
from items import DoubanGspiderItem


class MongodbPipeline(object):
    def __init__(self):
        import pymongo
        self._connection = pymongo.MongoClient(MONGODB_URI)
        self._zhihu_db = self._connection['zhihu']
        self._zhihu_users = self._zhihu_db['users']
        self._zhihu_questions = self._zhihu_db['questions']

        self._douban_db = self._connection['douban']
        self._douban_groups = self._douban_db['groups']

    def process_item(self, item, spider):
        if isinstance(item, ZhihuspiderItem):
            self._saveZhihu(item, spider)
        if isinstance(item, ZhihuQspiderItem):
            self._saveZhihuQ(item, spider)
        if isinstance(item, DoubanGspiderItem):
            self._saveDoubanG(item, spider)
        if isinstance(item, ZhihuUserspiderItem):
            self._saveZhihuUser(item, spider)
        return item

    def _saveZhihu(self, item, spider):
        self._zhihu_users.insert(item)

    def _saveZhihuQ(self, item, spider):
        question_info = self._zhihu_questions.find_one({'question_id': item['question_id']})
        if not question_info:
            self._zhihu_questions.insert(item)

    def _saveZhihuUser(self, item, spider):
        user_info = self._zhihu_users.find_one({'account': item['account']})
        if not user_info:
            self._zhihu_users.insert(item)

    def _saveDoubanG(self, item, spider):
        group_info = self._douban_groups.find_one({'group_id': item['group_id']})
        if not group_info:
            self._douban_groups.insert(item)
