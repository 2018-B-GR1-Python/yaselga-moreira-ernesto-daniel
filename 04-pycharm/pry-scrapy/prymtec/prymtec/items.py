# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Producto(scrapy.Item):
    titulo = scrapy.Field()
    precio = scrapy.Field()
    link = scrapy.Field()
    pass
