import scrapy

class GeniusSpider(scrapy.Spider):
    name = "genius"
    start_urls = [
        "https://genius.com/Big-sean-nothing-is-stopping-you-lyrics"
    ]

    def parse(self, response):
        lyrics_container = response.css('div[data-lyrics-container="true"]')

        for fragment in lyrics_container.css('.ReferentFragmentdesktop__ClickTarget-sc-110r0d9-0.cehZkS'):
            yield {
                'fragment': fragment.css('span.ReferentFragmentdesktop__Highlight-sc-110r0d9-1.jAzSMw::text').get()
            } 

        #next_page = response.css("li.next a::attr(href)").get()
        
        #if next_page is not None:
            #yield response.follow(next_page, callback=self.parse)