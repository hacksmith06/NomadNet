import scrapy
from myspider.items import H3TagItem  # Replace 'myproject' with your project name


class H3Spider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['traveltriangle.com']
    start_urls = ['https://traveltriangle.com/blog/places-to-visit-in-india-before-you-turn-30/']

    def parse(self, response):
        for h3 in response.css('h3'):
            item = H3TagItem()
            item['content'] = h3.css('::text').get()
            yield item
