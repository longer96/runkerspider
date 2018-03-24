# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from runkerspider.items import ArticleItem


class RunkerSpider(scrapy.spiders.Spider):
    # 定义爬虫名 之后在执行scrapy crawl runker
    name = "runker"
    # 允许访问的域名范围，规定爬虫只爬取这个域名下的网页
    allowed_domain = ["runker.net"]
    # 要爬取的网站
    start_urls = [
        "http://www.runker.net/page/1",
        # "http://www.runker.net/page/2",
        # "http://www.runker.net/page/3",
        # "http://www.runker.net/page/4",
        # "http://www.runker.net/page/5",
        # "http://www.runker.net/page/6",
        # "http://www.runker.net/page/7",
        # "http://www.runker.net/page/8",
        # "http://www.runker.net/page/9",
        # "http://www.runker.net/page/10"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # forsite in response.xpath('//div[@class="content"]')
        # site = response.xpath('/html/head/title').extract()
        # 写入文件
        # open("content.txt","w").write(site)

        # for site in response.xpath('//div[@id="content"]'):
        # 	print site.xpath().extract()[0]
        # 	print "==========="
        # response.xpath('//img/@src'):
        # open("content.txt","w").write(response.xpath('//div[@class="content"]').extract()[0])
        # title = site.xpath('div/img/@src').extract()
        # title = site.xpath('dl/dd/h2/a/text()').extract()
        # for t in title:
        # 	print t
        # if(len(title) > 0):
        # 	print title[0].encode('IOS 8859-1')
        # s遍历获得的url，如果满足条件，继续爬取
        # yield Request("http://www.runker.net/page/2", callback=self.parse)

        print "===========begin======" + response.url
        for i, art in enumerate(response.xpath('//div[@id="content"]/div')):
            # 先去除不是文章列的 开头和结尾
            if i == 0 or i == 19:
                continue

            item = ArticleItem()

            art_title = art.xpath('dl/dd/h2/a/text()').extract()
            art_url = art.xpath('dl/dd/h2/a/@href').extract()
            art_imgurl = art.xpath('dl/dt//img/@src').extract()

            print "title:" + art_title[0]
            print "url:" + art_url[0]
            if len(art_imgurl):
                print "img_url:" + art_imgurl[0]

            item['title'] = art_title[0]
            item['url'] = art_url[0]
            item['image_urls'] = art_imgurl
            print "---------------------"
            yield item
        # yield Request("http://www.runker.net/page/2", callback=self.parse)
        print "===========end==========="
