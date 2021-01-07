import requests
from bs4 import BeautifulSoup


def parse(params=None):
    URL = "https://shop.kz/noutbuki/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
    }
    response = requests.get(URL, headers=HEADERS, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='bx_catalog_item double')
    comps = []  
    for item in items:        
        comps.append({
            'title': item.find('div', class_='bx_catalog_item_title').find_next('a').get_text(strip=True),
            'price': item.find('span', class_='bx-more-price-text').get_text(strip=True)
        })
    for comp in comps:
        print('\t',comp['title'], '-->', comp['price'])
            

parse()

