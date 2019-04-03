import scrapy
from tutorial.items import NavItem
from scrapy.loader import ItemLoader

class JokeSpider(scrapy.Spider):
    name = "navspider"
    start_urls = [
        'http://www.laughfactory.com/jokes'
    ]

    def parse(self, response):
        for text in response.xpath("//div[@class='jokes-nav']/ul/li"):
            l= ItemLoader(item=NavItem(), selector=text)
            l.add_xpath('nav_text', ".//div[@class='jokes-nav']/ul/li/a/text()")
            yield l.load_item()

#valamiért üres sort szed ki és idk why