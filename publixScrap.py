import scrapy
from ..items import PublixscrapItem


class publixSpider(scrapy.Spider):
    
    name = 'publix'

    start_urls = [
        'https://www.publix.com/locations/1048-baldwin-park'
    ]




  
    def parse(self, response, dont_filter = True):

        


        allItems = response.css('.top-section, .title, p-savings-badge__text .color--null ')

        items = PublixscrapItem()

        for publix in allItems:




            food = publix.css('.title::text').extract()
            dealType = publix.css('.p-savings-badge__text .color--null::text').extract()

            items['food'] = food
            items['dealType'] = dealType
        

            yield items

        next_page = response.css('.cta-link a::attr(href)').get()

        if next_page is not None: 
            yield response.follow(next_page)  

        list_view =  'https://www.publix.com/savings/weekly-ad/view-all'
        if list_view is not None:

            yield response.follow(list_view, callback = self.parse)








# import scrapy
# from ..items import QuotetutorialItem
# class QuoteSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = [
#         'http://quotes.toscrape.com/'
#     ]

#     def parse(self, response):
#         all_div_quotes = response.css('div.quote')

#         items = QuotetutorialItem()

#         for quote in all_div_quotes:




#             title = quote.css('span.text::text').extract()
#             author = quote.css('.author::text').extract()
#             tag = quote.css('.tag::text').extract()

#             items['title'] = title
#             items['author'] = author
#             items['tag'] = tag

#             yield items

#         next_page = response.css('li.next a::attr(href)').get()

#         if next_page is not None: 
#             yield response.follow(next_page, callback = self.parse)   