# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class memberitem(scrapy.Item):
    job_title = scrapy.Field()
    experience = scrapy.Field()
    location = scrapy.Field()
    company_name = scrapy.Field()
    job_description_link = scrapy.Field()
    keyskills = scrapy.Field()
    jdescp = scrapy.Field()
    salary = scrapy.Field()
