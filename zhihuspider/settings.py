# -*- coding: utf-8 -*-

# Scrapy settings for zhihuspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import os

BOT_NAME = 'zhihuspider'
BASE_DIR = os.getcwd()

SPIDER_MODULES = ['zhihuspider.spiders']
NEWSPIDER_MODULE = 'zhihuspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuspider (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuspider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihuspider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihuspider.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

ITEM_PIPELINES = {
    'zhihuspider.pipelines.MongodbPipeline': 1000,
}

MONGODB_URI = 'mongodb://127.0.0.1:27017'

HEADER={
    "Host": "www.zhihu.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
}
COOKIES = {
    '_za': r'00c48e09-51ab-454c-8316-f3bd46dd3c69',
    '_ga': r'GA1.2.1494950905.1434349188',
    'q_c1': r'a6c0245f8cce45fe8da895f2e96f7362|1438333731000|1432634306000',
    '_xsrf': r'2baad1267223df9f93a89ac28446e76f',
    'tc': r'AQAAAFfzIV0yuQMAmqQ/t515NIjl+6PT',
    'cap_id': r'"NjU1YjhmNDgyMzAyNDA4ZmFkY2NiYmE3MDA0ZjkyNjE=|1439778230|1b241318b87939ba52c712db38a333459024fe03"',
    '__utmt': r'1',
    'z_c0': r'"QURBRGFLNXMxZ2NYQUFBQVlRSlZUWHV3QTFiOWxzb2V6THJJbWgwWDAtV29KT3ZUM2Y4TUxBPT0=|1440490364|6d25cf4373c7d7ceded7b13591b72511e1c36807"',
    'unlock_ticket': r'"QURBRGFLNXMxZ2NYQUFBQVlRSlZUWU1xM0ZYRmVUN0poNWVYbGhXZUhmMGpJUXFIY0dTUjFBPT0=|1440490364|ba96d4b8ef5ba62555e22a7e0995dbbc26e20f0c"',
    '__utma': r'51854390.1494950905.1434349188.1440490482.1440490482.1',
    '__utmb': r'51854390.12.10.1440490482',
    '__utmc': r'51854390',
    '__utmz': r'51854390.1440490482.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utmv': r'51854390.100--|2=registration_date=20150327=1^3=entry_date=20150327=1',
}