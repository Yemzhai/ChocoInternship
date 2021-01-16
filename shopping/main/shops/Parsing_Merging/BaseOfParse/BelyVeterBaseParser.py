import requests
from bs4 import BeautifulSoup


class BelyVeterParser(object):
    def __init__(self, bely_veter_items, url, pages):
        self.bely_veter_items = bely_veter_items
        self.url = url
        self.pages = pages

    def parse(self):
        item_from = "bely veter"
        for page in range(1, self.pages):
            print(page, "- Bely veter page is ready!")

            URL = f"{self.url}={page}"
            HEADERS = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
            }
            response = requests.get(URL, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.findAll('div', class_='bx_catalog_item double')
            for item in items:
                name = item.find('div', class_='bx_catalog_item_title').find_next('a').get_text(strip=True),
                price = item.find('span', class_='bx-more-price-text').get_text(strip=True)

                information = str(name[0]+' price: '+price+' from: '+item_from)
                self.bely_veter_items.append(information)


def get_start_bely_veter(url, pages):
    bely_veter_items = []
    bely_veter_parser = BelyVeterParser(bely_veter_items, url, pages)
    bely_veter_parser.parse()
    return bely_veter_items
