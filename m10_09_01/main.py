import json
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

base_url = "https://index.minfin.com.ua/ua/russian-invading/casualties"


def get_urls():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class=ajaxmonth] h4[class=normal] a')
    urls = ['/']
    prefix = '/month.php?month='
    for a in content:
        url = prefix + re.search(r'\d{4}-\d{2}', a['href']).group()
        urls.append(url)
    return urls


def spider(urls):
    data = []
    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('ul[class=see-also] li[class=gold]')
        for el in content:
            result = {}
            date = el.find('span', attrs={"class": "black"}).text
            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()
            except ValueError:
                print(f'Error for date: {date}')
                continue
            result.update({'date': date})
            losses = el.find('div').find('div').find('ul')
            for l in losses:
                name, quantity, *_ = l.text.split('—')
                name = name.strip()
                quantity = int(re.search(r'\d+', quantity).group())
                result.update({name: quantity})
            data.append(result)
    return data


if __name__ == '__main__':
    url_for_scraping = get_urls()
    print(url_for_scraping)
    r = spider(url_for_scraping)
    with open('enemy.json', 'w', encoding='utf-8') as fd:
        json.dump(r, fd, ensure_ascii=False)

