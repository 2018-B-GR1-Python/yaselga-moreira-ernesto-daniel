import scrapy
from prymtec.items import Producto

class Spider_Producto(scrapy.Spider):
    name = 'fb_items'

    start_urls = [
        'https://www.facebook.com/pg/MTEC-172463372806603/shop/?ref=page_internal&search_text=Procesador'
        ]

    def parse(selfself, response):
        lista_procesadores = response.css('tr > td > div > div > div')


        for procesador in lista_procesadores:
            titulo  = response.css('a > strong:nth-child(1)::text').extract_first()
            precio  = response.css('div:nth-child(2)::text').extract_first()
            link    = response.css('a::attr(href)').extract_first()


            titulo_truncado = titulo
            link_completo =  "https://www.facebook.com"+link

            item =  Producto()
            item['titulo'] = titulo_truncado
            item['precio'] = precio
            item['link'] = link_completo

            print(item['titulo'])

            yield item