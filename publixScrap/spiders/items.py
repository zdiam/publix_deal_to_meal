# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PublixscrapItem(scrapy.Item):
    food = scrapy.Field()
    dealType = scrapy.Field()
    link = scrapy.Field()
    pass


class PublixscrapType(scrapy.Item):
    url = scrapy.Field()
    dealT = scrapy.Field()

    pass
