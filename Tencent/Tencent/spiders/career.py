# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class CareerSpider(scrapy.Spider):
    name = 'career'
    allowed_domains = ['tencent.com']
    url = "https://careers.tencent.com/search.html?index="
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        print(response.body)
        node_list = response.xpath("//a[@class='recruit-list-link']")

        for node in node_list:
            item = TencentItem()
            item['position'] = node.xpath("./h4/text()").extract_first()
            item['positionContent'] = node.xpath("./p[@class='recruit-text']/text()").extract_first()
            tips = node.xpath("./p[@class='recruit-tips'].text()")
            print(len(tips))


