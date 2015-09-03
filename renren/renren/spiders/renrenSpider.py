
import scrapy
from scrapy.spiders import Rule
from scrapy.http import Request, FormRequest
from scrapy.linkextractors import LinkExtractor
from renren.items import RenrenItem


class renrenImageSpider(scrapy.Spider):

    """Docstring for renrenImageSpider. """
    name = "renren"
    allowed_domains = ["http://renren.com/"]
    login_page = "http://www.renren.com/plogin.do"
    start_urls = [
        # "http://github.com/zeyue/",
        # "http://zeyue.wordpress.com"
        "http://www.renren.com/237977740"
    ]
    rules = (
        Rule(LinkExtractor(allow=r'-\w+.html$'),
             callback='parse', follow=True),
    )

    def init_request(self):
        """TODO: Docstring for init_request.
        :returns: TODO

        """
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        """TODO: Docstring for login.

        :response: TODO
        :returns: TODO

        """
        return FormRequest.from_response(response,
                                         formdata={
                                             'email': '',
                                             'password': ''},
                                         callback=self.check_login_response)

    def check_login_response(self, response):
        """TODO: Docstring for check_login_response.

        :response: TODO
        :returns: TODO

        """
        if "Hi Zeyue" in response.body:
            self.log("Successfully logged in. Let's start crawling!")
            self.initialized()
        else:
            self.log("Bad times...")

    def parse(self, response):
        """TODO: to be defined1. """
        item = RenrenItem()
        for sel in response.xpath('//img'):
            item['image_urls'] = sel.xpath('@src').extract()
            yield item
