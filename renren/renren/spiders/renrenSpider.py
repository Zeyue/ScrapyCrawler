
import scrapy
from renren.items import RenrenItem


class renrenImageSpider(scrapy.Spider):

    """Docstring for renrenImageSpider. """
    name = "renren"
    allowed_domains = ["http://renren.com/"]
    start_urls = [
        "http://tieba.baidu.com/p/2166231880"
    ]

    def parse(self, response):
        """TODO: to be defined1. """
        item = RenrenItem()

        item['image_urls'] = response.xpath("//cc/div/img[@class \
='BDE_Image']/@src").extract()
        return item
