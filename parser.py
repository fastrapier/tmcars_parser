import csv

import requests
from bs4 import BeautifulSoup
import re
from model import Ad


class Parser:
    def __init__(self, search_word):
        self._search_word = search_word
        self._ads = list()

    def parse(self):
        headers = {
            'x-requested-with': 'XMLHttpRequest',
        }

        params = (
            # ('offset', '150'),
            ('max', '10000'),
            ('mask', self._search_word),
            ('latest', 'true'),
            ('includePhoto', 'true'),
            ('lang', 'ru'),
        )

        response = requests.get('https://tmcars.info/others/all', headers=headers, params=params)

        soup = BeautifulSoup(response.text, 'lxml')

        products_table = soup.select('div#otherProductTable > div')

        for elem in products_table:
            ad = Ad()

            try:
                url = elem.find('a')

                if url is None:
                    continue
                else:
                    url = url.get('href')

                ad.url = url
                # print(ad.url)

                title = elem.select_one('a > h5').text
                if not re.search(self._search_word, title, re.IGNORECASE):
                    continue

                ad.title = title
                # print(ad.title)

                price = elem.select_one('div.item-card2-desc > span.h5')

                if price is None:
                    continue

                price = price.text.replace('TMT', "").strip()
                ad.price = price
                # print(ad.price)

                descr = elem.select_one('div.item-card2-desc > p.max-lines-p-desc').text
                ad.descr = descr
                # print(ad.descr)

                city = elem.select_one('div.item-card2-desc > div > p').text
                ad.city = city
                # print(ad.city)

                published = elem.select_one('div.item-card2-desc > div > span').text
                ad.published = published
                # print(ad.published)

                self._ads.append(ad)

            except AttributeError as e:
                print(f'Error: {e}')
                print(elem)
                break

    def serialize_into_csv(self):
        with open("ads.csv", 'w', encoding='UTF-8', newline='') as stream:
            writer = csv.writer(stream)
            writer.writerow(['Published', 'Title', 'Price', "City", "Descr", "Url"])
            writer.writerows(self._ads)
