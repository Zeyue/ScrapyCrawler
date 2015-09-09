# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request


class RenrenPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        """TODO: Docstring for get_mediia_requests.

        :item: TODO
        :info: TODO
        :returns: TODO

        """
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        """TODO: Docstring for item_completed.

        :results: TODO
        :item: TODO
        :info: TODO
        :returns: TODO

        """
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['images'] = image_paths
        return item
