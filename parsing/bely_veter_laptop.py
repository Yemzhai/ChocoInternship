import requests
from bs4 import BeautifulSoup


class BelyVeterParser():
    def __init__(self, bely_veter_items):
        self.bely_veter_items = bely_veter_items

    def parse(self, params=None):
        item_from = "bely veter"
        for page in range(1, 2):
            print(page, "- Bely veter page is ready!")

            URL = "https://shop.kz/noutbuki/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1={}".format(page)
            HEADERS = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
            }
            response = requests.get(URL, headers=HEADERS, params=params)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.findAll('div', class_='bx_catalog_item double')
            for item in items:
                name = item.find('div', class_='bx_catalog_item_title').find_next('a').get_text(strip=True),
                price = item.find('span', class_='bx-more-price-text').get_text(strip=True)

                information = str(name[0]+' price: '+price+' from: '+item_from)
                self.bely_veter_items.append(information)



bely_veter_items = []
bely_veter_parser = BelyVeterParser(bely_veter_items)
bely_veter_parser.parse()

# for i in bely_veter_items:
#     print(i)
