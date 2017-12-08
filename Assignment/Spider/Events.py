# -*- coding: utf-8 -*-
import scrapy
import os
import platform
import csv
import collections
from tqdm import tqdm


class EventsSpider(scrapy.Spider):

    name = "events"
    allowed_domains = ["http://46.101.108.154"]
    start_urls = ["http://46.101.108.154/"]
    base_urls = ["http://46.101.108.154/"]

    @classmethod
    def from_crawler(self, crawler):
        zpider = self()
        crawler.signals.connet(zpider.spider_opened, signal=scrapy.signals.spider_opened)
        return zpider

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for x in result:
            yield x

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_request(self, start_requests, spider):
        for y in start_requests:
            yield y

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

    def decision_save_to_single_file(self):
        self.setup_file()

    def decision_save_to_seperate_files(self):
        self.setup_file_split_zips()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        crawl_pages = response.xpath('//a/@hrf').extract()
        page_amount = len(crawl_pages)

        self.pbar = tqdm(total=page_amount)
        self.pbar.clear()

        for page in crawl_pages:
            yield scrapy.Request(self.base_url + page, callback=self.parse_page)


            pass


    def parse_page(self, response):
        data_rows = []
        rows = response.css("tr")

        for row in rows:
            data_row = (
                row.xpath("td[1]/h3/b/font/text()[1]").extract.first(),
                row.xpath("td[1]/span[1]/b/text()[1]").extract.first(),
                row.xpath("td[1]/span[1]/text()[1]").extract.first(),
                row.xpath("td[1]/span[2]/a/text()[1]").extract.first(),
            )

        '#temp_string = data_row[3].Split()[1]'
        data_row[3] = data_row[3].Split()[1]


        if self.zip_split is "y":
            self.save_rows_seperate(data_rows, "zipName")

def save_rows_seperate(self, data_rows):
    None
