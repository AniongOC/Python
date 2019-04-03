import scrapy
from tutorial.items import JokeItem
from scrapy.loader import ItemLoader

class JokeSpider(scrapy.Spider):
    name = "jokespider"
    start_urls = [
        'http://www.laughfactory.com/jokes/family-jokes'
    ]

    def parse(self, response):
        for joke in response.xpath("//div[@class='jokes']"):
            l= ItemLoader(item=JokeItem(), selector=joke)
            l.add_xpath('joke_text', ".//div[@class='joke-text']/p")
            yield l.load_item()

        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)