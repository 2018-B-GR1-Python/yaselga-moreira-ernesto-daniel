import scrapy
from BtcHw.items import Btcitem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

class Spider_Registros(scrapy.Spider):
    name = 'btc_registros'

    start_urls = [
        'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20190207'
        ]

    def parse(selfself, response):
        tablabtc = response.css('.text-right')

        for registro in tablabtc:
            registro_loader = ItemLoader(
                item = Btcitem(),
                selector = registro
            )

            registro_loader.default_output_processor = TakeFirst()
            #registro_loader.default_output_processor = MapCompose()

            date = registro_loader.add_css('date', 'tr.text-right > td:nth-child(1)::text')
            open = registro_loader.add_css('open', 'tr.text-right > td:nth-child(2)::text')
            high = registro_loader.add_css('high', 'tr.text-right > td:nth-child(3)::text')
            low = registro_loader.add_css('low', 'tr.text-right > td:nth-child(4)::text')
            close = registro_loader.add_css('close', 'tr.text-right > td:nth-child(5)::text')
            volume = registro_loader.add_css('volume', 'tr.text-right > td:nth-child(6)::text')
            marketCap = registro_loader.add_css('marketCap', 'tr.text-right > td:nth-child(7)::text')

            # print(date, open, close)
            yield registro_loader.load_item()