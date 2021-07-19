 # -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.http import Request
from fia.items import FiaItem

class ChapterSpider(Spider):
    name = 'chapter'
    allowed_domains = ['polyglot.sps.edu']
    start_urls = ['http://polyglot.sps.edu/audio/french/fia_2e/chapitre_16/index.php']

    # def parse(self, response):
    #     chap_links = response.xpath('//td/a/@href').extract()
    #     # './chapitre_02/index.php'
    #     # https://polyglot.sps.edu/audio/french/fia_2e/index.php
    #     # https://polyglot.sps.edu/audio/french/fia_2e/chapitre_02/index.php
    #     for chap_link in chap_links:
    #         chap_link = chap_link.replace('./', '')
    #         base='https://polyglot.sps.edu/audio/french/fia_2e/'
    #         abs_chap_link = base + chap_link
    #         # print (abs_chap_link)
    #         yield Request(abs_chap_link, callback=self.parse_mp3)
# 'polyglot.sps.edu/audio/french/fia_2e/index.php
# luon phai kiem tra allowed_domains so voi domain o yield scrapy.Request
    # def parse_mp3(self, response):
    #               # https://polyglot.sps.edu/audio/french/fia_2e/chapitre_02/2.01-b_Text_work-up_01-02.mp3          
    #     base_chap = response.request.url.replace('index.php', '')
    #     mp3_collection = response.xpath('//source/@src').extract()
    #     # print(mp3_collection)
    #     for mp3_name in mp3_collection:
    #         abs_mp3_name = base_chap + mp3_name
    #         l = ItemLoader(item=FiaItem(), selector = mp3_name)
    #         # print(abs_mp3_name)
    #         l.add_value('file_name', mp3_name)
    #         l.add_value('file_urls', abs_mp3_name)
    #         yield l.load_item()

    def parse(self, response):
                  # https://polyglot.sps.edu/audio/french/fia_2e/chapitre_02/2.01-b_Text_work-up_01-02.mp3          
        base_chap = response.request.url.replace('index.php', '')
        mp3_collection = response.xpath('//source/@src').extract()
        # print(mp3_collection)
        for mp3_name in mp3_collection:
            abs_mp3_name = base_chap + mp3_name
            l = ItemLoader(item=FiaItem(), selector = mp3_name)
            # print(abs_mp3_name)
            l.add_value('file_name', mp3_name)
            l.add_value('file_urls', abs_mp3_name)
            yield l.load_item()
