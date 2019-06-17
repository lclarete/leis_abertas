# -*- coding: utf-8 -*-
import scrapy

# define pagination
# final pagination number
n_final = 5520

# range of number pages fom 0 to n_final 30 by 30 -- accordingly to Interlegis pagination
list_page_n = [i for i in range(0, n_final, 30)]
# initial link
url = 'http://www.interlegis.leg.br/institucional/casas-conveniadas/municipal?b_start:int='
# create new links with page numbers
urls = [url+str(i) for i in list_page_n]

class CityLinksSpider(scrapy.Spider):
    name = 'city_links'
    start_urls = urls
    def parse(self, response):
        item = response.xpath('//a/@href').extract()
        list_item = []
        for i in item:
            if 'id=' in i:
                list_item.append(i)
        yield {'links':list_item}

        