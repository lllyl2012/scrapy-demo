# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def process_item(self, item, spider):
        data = json.dumps(dict(item.body), ensure_ascii=False)
        print(data)
        return item
