# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sohu.items import SohuItem



class ShSpider(CrawlSpider):
    name = 'sh'
    allowed_domains = ['sohu.com']
    start_urls = ['http://www.sohu.com/c/8/1460']
    times=0

    rules = (
        Rule(LinkExtractor(allow='/c/8/1460'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        for sel1 in response.xpath('//div[@data-role="news-item"]/h4/a/@href').extract():
            group_url=response.urljoin(sel1)
            yield scrapy.Request(url=group_url,callback=self.parse_url,dont_filter=True)

    def parse_url(self,response):
        item=SohuItem()
        item["context"]=response.xpath('//article[@class="article"]/p/text()').extract()
        print(item["context"])
        # title=item["context"][0]
        #fh = open("D:/file/python_learning/CH5/news/" + str(self.times) + ".txt", "wb")
        self.times +=1
        #print(self.times)
        #fh.write(context)
        yield item

