import scrapy
from prymtec.items import Producto
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

class Spider_Producto(scrapy.Spider):
    name = 'mtec_items'

    start_urls = [
        'https://www.mtec-ec.com/categoria-producto/procesadores/',
        'https://www.mtec-ec.com/categoria-producto/procesadores/page/2/',
        'https://www.mtec-ec.com/categoria-producto/procesadores/page/3/',
        'https://www.mtec-ec.com/categoria-producto/procesadores/page/4/'
        ]

    def parse(selfself, response):
        lista_productos = response.css('.details_product_item')

        for producto in lista_productos:

            producto_loader = ItemLoader(
                item = Producto(),
                selector = producto
            )

            producto_loader.default_output_processor = TakeFirst()

            titulo  = producto_loader.add_css('titulo', 'div > a > h5::text')
            precio  = producto_loader.add_css('precio', 'span:nth-child(3) > span:nth-child(1)::text')
            link    = producto_loader.add_css('link', 'div > a::attr(href)')
            print(titulo, precio, link)
            yield producto_loader.load_item()