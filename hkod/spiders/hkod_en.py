# -*- coding: utf-8 -*-
import scrapy
from hkod.items import HkodItem
import datetime

def getDataInfo():
    hkodItem = HkodItem()
    
    

    return hkodItem


class HkodEnSpider(scrapy.Spider):
    name = 'hkod_en'
    allowed_domains = ['data.gov.hk']
    start_urls = ['https://data.gov.hk/en-datasets/']
    file_name = datetime.datetime.now().strftime("%F") +"_en.csv"
 
    def parse(self, response):
        cats = response.xpath('//*[@id="category-list"]/nav/ul/li')
        for cat in cats:
            link = cat.css("a::attr(href)").extract_first()
            name = cat.css("a::attr(title)").extract_first()
            link = response.urljoin(link)
            self.log(link)
            self.log(name)
            if (name == "Development" or name == "Food"):
                request = scrapy.Request(link, callback=self.parse_cat_listing)
                request.meta['cat_link'] = link
                request.meta['category'] = name
                yield request
        
    def parse_cat_listing(self, response):
        cat_link = response.meta['cat_link']
        category = response.meta['category']
    
        datasets = response.css(".dataset-item")
        self.log("Dataset size: {}".format(len(datasets)))
        
        for dataset in datasets:
            name = dataset.css(".dataset-heading a::text").extract_first()
            link = dataset.css(".dataset-heading a::attr(href)").extract_first()
            link = response.urljoin(link)
            self.log(" Name: {}".format(name))
            org =  dataset.css(".organization a::text").extract_first()
            self.log(" Organization: {}".format(org))
            formats = dataset.css(".dataset-resources.list-unstyled li a::text").extract()
            data_format = "/".join(formats)
#            data_format = '/'.join(map(str, formats)) 
            self.log(" Format Len: {}".format(len(formats)))
            self.log(" Formats: " + data_format)
            request = scrapy.Request(link, callback=self.parse_dataset_detail)
            yield request
#           getDataInfo(category)
        
        load_more = response.css("#load-more").extract_first()
#        self.log(load_more)
        if load_more is not None:
            page_number = response.css("#load-more::attr(data-next-page)").extract_first()
            next_link = cat_link + " &page=" + page_number
            self.log("load more {}".format(next_link))        
            request = scrapy.Request(next_link, callback=self.parse_cat_listing)
            request.meta['cat_link'] = cat_link
            request.meta['category'] = category
            yield request
        else:
            self.log("No more")
           
    def parse_dataset_detail(self, response):     
        update_freq = response.css(".update-frequency-area ::text").extract_first() 
        self.log(" UD Freq>"+update_freq)