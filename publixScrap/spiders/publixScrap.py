import scrapy
from scrapy.crawler import CrawlerProcess
from items import PublixscrapItem
# from scrapy.utils.project import get_project_settings

# process = CrawlerProcess(get_project_settings)


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

process = CrawlerProcess(settings={
    "FEEDS": {
        "items2.csv": {"format": "csv"},
    },
})

process.crawl(publixSpider)
process.start()






  