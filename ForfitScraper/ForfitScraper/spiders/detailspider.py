import scrapy
from ..utils import load_links
from bs4 import BeautifulSoup


def inner_text(selector):
    html = selector.get()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text().strip()


class DetailSpider(scrapy.Spider):
    name = 'detail'
    start_urls = load_links('products.json')

    def parse(self, response):
        for product in response.css('div.column.main'):
            main_info = product.css('div.product-info-main')
            title_wrapper = main_info.css('div.page-title-wrapper.product')
            title = title_wrapper.css('h1.page-title')
            info_price = main_info.css('div.product-info-price')
            info_stock_sku = info_price.css('div.product-info-stock-sku')
            attribute_sku = info_stock_sku.css('div.product.attribute.sku')
            media_info = product.css('div.product.media')
            gallery_placeholder = media_info.css('div.gallery-placeholder._block-content-loading')
            image_link = gallery_placeholder.css('a.product-image-link')
            photo_link = image_link.css('img::attr(src)').get()
            description = product.css('div.product.attribute.description')
            description_value = inner_text(description.css('div.value'))
            additional_attributes = product.css('div.additional-attributes-wrapper.table-wrapper')
            table_attributes = additional_attributes.css('table.scrapped_data.table.additional-attributes')
            tbody = table_attributes.css('tbody')
            trs = dict()
            for tr in tbody.css('tr'):
                info = tr.css('th::text').get().lower()
                if info != 'identyfikator':
                    trs[info] = tr.css('td::text').get()
            yield {
                'big-photo': photo_link,
                'name': title.css('span.base::text').get(),
                'sku': attribute_sku.css('div.value::text').get(),
                'description': description_value,
                'additional_information': trs
            }
