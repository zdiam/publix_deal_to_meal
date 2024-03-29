import scrapy
from scrapy.crawler import CrawlerProcess
from items import PublixscrapItem
from items import PublixscrapType




class publixSpider(scrapy.Spider):
    
    name = 'publix'


 
    start_urls = [
        'https://accessibleweeklyad.publix.com/PublixAccessibility/Entry/LandingContent?storeid=2501005&sneakpeek=N&listingid=0'
    ]

    listing = [
        '.leftcolumn .listing::attr(href)',
    ]


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_recurse, cb_kwargs={"listing": self.listing})



    def parse_recurse(self, response, listing):


        first = listing[0]
        rest  = listing[1:]
        
        links = response.css(first).extract()
        
        if rest:
            for link in links:
                yield response.follow(link, callback=self.parse_recurse, cb_kwargs={"listing": rest})
        else:

            for link in links:
                yield response.follow(link, callback=self.parse)



  
    def parse(self, response, dont_filter = True):

 


        allItems = response.css('.theTile')
        items = PublixscrapItem()

        for publix in allItems:




            food = publix.css('.title .ellipsis_text::text').extract()
            dealType = publix.css('.deal .ellipsis_text::text').extract()
            


            
            
            items['link'] = response.request.url
            


 

            items['food'] = food
            items['dealType'] = dealType

           

        

            yield items


class publixUrl(scrapy.Spider):
    
    name = 'publixUrl'

    start_urls = [
         'https://accessibleweeklyad.publix.com/PublixAccessibility/Entry/LandingContent?storeid=2501005&sneakpeek=N&listingid=0'
    ]




    def parse(self, response, dont_filter = True):

        allItems = response.css('.leftcolumn .listing')
        items = PublixscrapType()

        for publix in allItems:
        
  


            url = publix.css('::attr(href)').extract()

            dealT = publix.css('*::text').extract()

            items['url'] = url

            items['dealT'] = dealT

            yield items


processA = CrawlerProcess(settings={
    "FEEDS": {
        "itemsA.csv": {
        "format": "csv",
        "overwrite": True
        },
        
    },
})

processB = CrawlerProcess(settings={
    "FEEDS": {
        "itemsB.csv": {
        "format": "csv",
        "overwrite": True},
        
    },
})



processA.crawl(publixSpider)
processB.crawl(publixUrl)
processA.start()
processB.start()





  