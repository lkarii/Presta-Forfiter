import scrapy


class CategorySpider(scrapy.Spider):
    name = 'category'
    start_urls = ['https://www.forfiterexclusive.pl/']

    def parse(self, response):
        for category in response.css('li.ui-menu-item.level1'):
            yield {
                'name': category.css('a::text').get(),
                'link': category.css('a').attrib['href']
            }
