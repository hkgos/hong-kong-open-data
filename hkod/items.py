# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HkodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    category = scrapy.Field()
    name = scrapy.Field()
    org = scrapy.Field()
    data_format = scrapy.Field()        
    update_feq = scrapy.Field()   
    desc = scrapy.Field()   
    api = scrapy.Field()   
 
    pass
