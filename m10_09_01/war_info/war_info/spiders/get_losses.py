import json
import re
from datetime import datetime

import scrapy


def get_next_link():
    with open('urls.json', 'r') as fd:
        r = json.load(fd)
    return [el.get('link') for el in r]


class GetLossesSpider(scrapy.Spider):
    name = "get_losses"
    allowed_domains = ["index.minfin.com.ua"]
    start_urls = ["https://index.minfin.com.ua/ua/russian-invading/casualties"]

    def parse(self, response, *_):
        result = {}
        content = response.css('ul[class=see-also] li[class=gold]')
        for el in content:
            date = el.xpath('span/text()').get()
            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()
            except ValueError:
                print(f'Error for date: {date}')
                continue

            result.update({'date': date})
            losses = el.xpath('div[@class="casualties"]/div/ul/li')
            for l in losses:
                print(''.join(l.css('*::text').extract()))
                name, quantity, *_ = ''.join(l.css('*::text').extract()).split('—')
                name = name.strip()
                quantity = int(re.search(r'\d+', quantity).group())
                result.update({name: quantity})

            yield result

        for next_link in get_next_link():
            yield scrapy.Request(self.start_urls[0] + next_link, method='GET')
