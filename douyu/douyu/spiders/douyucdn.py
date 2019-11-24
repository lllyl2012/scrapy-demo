# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DouyucdnSpider(scrapy.Spider):
    name = 'douyucdn'
    allowed_domains = ['douyucdn.cn']
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']
        # if not len(data_list):
        #     return
        for data in data_list:
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['avatar_mid'] = data['avatar_mid']

            yield item

        # self.offset += 20
        # yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
