import scrapy
from scrapy.crawler import CrawlerProcess


class NaverbikeSpider(scrapy.Spider):
    name = 'seek'
    allowed_domains = ['seek.com.au/welder-jobs/in-All-Perth-WA']
    start_urls = []

    def __init__(self):
        url = 'https://www.seek.com.au/welder-jobs/in-All-Perth-WA?page='
        for page in range(1, 3):
            self.start_urls.append(url + str(page))
        print(self.start_urls)

    def parse(self, response):
        title = response.css('h1 > a::text').getall()
        wage = response.css('.xKpxiM2').getall()


        print('response:', title, wage)
