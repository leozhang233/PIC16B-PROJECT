# scrapy crawl quotes_spider -o results.csv
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"

    start_urls = [
        "https://www.brainyquote.com/topics/fun-quotes"
    ]
    
    def parse(self, response):
        
        quotes = response.css("div[id^=pos] a div::text").getall()
        quotes = [q.strip() for q in quotes[::2]]
        author = response.css("div[id^=pos] a[title = 'view author']::text").getall()

        for q, a in zip(quotes, author):
            yield {
                "author" : a,
                "quote" : q
            }

        next_page = response.css("a.page-link")[-1].attrib['href']

        if next_page:
            next_page = "https://www.brainyquote.com" + next_page

            yield scrapy.Request(next_page, callback = self.parse)