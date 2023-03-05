import scrapy
from ..items import PublixscrapItem


class publixSpider(scrapy.Spider):
    
    name = 'publix'

    start_urls = [
        'https://accessibleweeklyad.publix.com/PublixAccessibility/BrowseByPage/Index/?Breadcrumb=Weekly+Ad&StoreID=2501005&PromotionCode=Publix-230223&PromotionViewMode=1'
    ]




  
    def parse(self, response, dont_filter = True):

        


        allItems = response.css('.theTile')
        items = PublixscrapItem()

        for publix in allItems:




            food = publix.css('.title .ellipsis_text::text').extract()
            dealType = publix.css('.deal .ellipsis_text::text').extract()

            items['food'] = food
            items['dealType'] = dealType
        

            yield items


            
        bogo_page = response.css('#CustomCategories a:nth-child(1)::attr(href)').get()

        if bogo_page is not None: 
            yield response.follow(bogo_page)  


##non functional
        # postbogo_page = response.css('.footerLink::attr(href)').get()

        # if postbogo_page is not None: 
        #     yield response.follow(postbogo_page)  

        # next_page = response.css('.exclude-role+ #CategoryFooterBar .action-tracking-nav::attr(href)').get()

        # if next_page is not None: 
        #     yield response.follow(next_page)  





  