import csv
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HkodPipeline(object):

    def open_spider(self, spider):
         self.file = csv.writer(open(spider.file_name, 'w', newline='', encoding = 'utf8') )
         fieldnames = ['Category', 'Name', 'Organization', 'Data Format', 'Update Frequency', 'Description', 'API']
         self.file.writerow(fieldnames)
#         print(" Spider name >>" + spider.name)

    def process_item(self, item, spider):
        self.file.writerow([item['category'], item['name'],item['org'], 
                    item['data_format'] , item['update_freq'],item['desc'], 
                    item['api']])

        return item
