import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        for card in response.css('div.quote'):
            yield {
                'text': card.css('span.text::text').get(),
                'author': card.css('small.author::text').get(),
                'tags': card.css('div.tags a.tag::text').getall()
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)