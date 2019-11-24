# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from douyu.settings import IMAGES_STORE

class DouyuPipeline(ImagesPipeline):
    # 获取图片
    def get_media_requests(self, item, info):
        image_link = item['avatar_mid']
        print(image_link + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        yield scrapy.Request(image_link)

    #保存存储信息
    def item_completed(self, results, item, info):
        path = [x["path"] for ok,x in results if ok]
        os.rename(IMAGES_STORE+path[0],IMAGES_STORE + item['nickname'] + ".jpg")
        return item

