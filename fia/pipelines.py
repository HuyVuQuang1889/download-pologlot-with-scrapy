# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
import re
from scrapy.http import Request
from urllib.parse import urlparse
from os.path import basename, dirname, join

class FiaPipeline(FilesPipeline):
    # def process_item(self, item, spider):
    #     return item

    def file_path(self, request, response=None, info=None):
        # 1 dong code duoi day la du tra ve ten file goc roi
        # return request.meta.get('filename', '')
        # 2 dong sau day tra ve thu muc moi theo ten duong dan ngay truoc ten file va ten file goc nhung phai xoa function get_media_requests de tranh download trung lap o thu muc mac dinh
        path = urlparse(request.url).path
        return join(basename(dirname(path)), basename(path))

        # hien code nay chua works vi ly do gi chua ro, rieng new_path hien se tra ve tenfile.mp3.mp3 can sua lai
        # original_path = super(FiaPipeline, self).file_path(request, response=None, info=None)
        # value_regex = re.compile("(?<=\/)(.*?)(?=\.)")
        # match = value_regex.search(original_path)
        # new_path = original_path.replace(match, request.meta.get('filename',''))
        # return new_path 

    # def get_media_requests(self, item, info):
        # de tranh bi loi request url must be str thi phai dung vong lap for de loop qua item['file_urls']k
        # file_url = item['file_urls'][0]
        # meta = {'filename': item['file_name'][0]}
        # yield Request(url=file_url, meta=meta)

