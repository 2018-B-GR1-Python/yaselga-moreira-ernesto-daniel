# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class PrymtecPipeline(object):
    def process_item(self, item, spider):
        return item

class ValidarProcesador(object):
    def process_item(self,item, spider):
        if('INTEL' not in item['titulo']):
            if('AMD' not in item['titulo']):
                raise DropItem('Error no es un procesador')
        elif ('COOLER' in item['titulo']):
            raise DropItem('Error no es un procesador')

        return item

