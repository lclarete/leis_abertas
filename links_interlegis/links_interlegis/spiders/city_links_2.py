# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

# open and read file
with open(r'links_final.csv', 'r') as file:
    links = file.readlines()

# split the elements from each line
list_links = [links[i].split(',') for i in range(1, len(links))]

# transform multiple lists into a single one
flat_list = [x for k in list_links for x in k]

# clean the list
flat_list_clean = [i.replace('"', "") for i in flat_list]

# remove duplicated elements
df = pd.DataFrame(flat_list_clean)
df.columns = ['col']
links = list(df.col.unique())

class CityLinks2Spider(scrapy.Spider):
    name = 'city_links2'
    start_urls = links
    def parse(self, response):
        item = {
            'title': response.xpath('//h1//text()').extract(),
            'url_camara': response.xpath('//dl[@class="casa"]//a/@href').extract(),
            'address': response.xpath('//dd[@class="portletItemSingle"]//span//text()').extract(),
            'link': response.xpath('//p[@class = "hiddenStructure"]//a//@href').extract()
        }
        yield(item)

