import scrapy


class Producto(scrapy.Item):
    Titulo = scrapy.Field()
    Precio = scrapy.Field()
    Link = scrapy.Field()
    pass