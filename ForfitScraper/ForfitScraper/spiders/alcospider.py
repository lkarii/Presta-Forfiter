import scrapy
from ..utils import load_links


class AlcoSpider(scrapy.Spider):
    name = 'alco'
    start_urls = load_links('categories.json')

    def parse(self, response):
        for product in response.css('div.product-item-info.type1'):
            photo = product.css('div.product.photo.product-item-photo')
            photo_a = photo.css('a')
            photo_link = photo_a.css('img::attr(data-src)').get()
            details = product.css('div.product.details.product-item-details')
            strong_link = details.css('strong.product.name.product-item-name')
            summary = details.css('div.product-reviews-summary.short')
            rating_summary = summary.css('div.rating-summary')
            rating_result = rating_summary.css('div.rating-result')
            rating = rating_result.css('span')
            final_price = details.css('div.price-box.price-final_price')
            category_title = response.css('div.category-title')
            yield {
                'photo': photo_link,
                'name': strong_link.css('a.product-item-link::text').get(),
                'link': strong_link.css('a.product-item-link').attrib['href'],
                'rating': rating.css('span::text').get(),
                'price': final_price.css('span.price::text').get(),
                'category': category_title.css('h1::text').get(),
            }
        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
