import requests
from bs4 import BeautifulSoup


def parse(params=None):
    URL = "https://www.sulpak.kz/f/noutbuki"
    BASE_URL = "https://www.sulpak.kz"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
    }
    response = requests.get(URL, headers=HEADERS, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='goods-tiles')
    comps = []  
    for item in items:
        availability = item.find('span', class_='availability').get_text(strip=True)
        if(availability=="Есть в наличии"):
            comps.append({
                'title': item.find('a').find_next('h3').get_text(strip=True),
                'price': item.find('div', class_='price').get_text(strip=True),
                'availability': item.find('span', class_='availability').get_text(strip=True),
                'link': BASE_URL+item.find('a').get('href')
            })
        elif(availability=='Нет в наличии'):
            comps.append({
                'title': item.find('a').find_next('h3').get_text(strip=True),
                'price': 'None',
                'availability': item.find('span', class_='availability').get_text(strip=True),
                'link': BASE_URL+item.find('a').get('href')
            })

        for comp in comps:
            print(comp['title'], '-->', comp['price'], 'availability: ', comp['availability'],'#', comp['link'])

for i in range (1,13):
    parse(params={'page':i})

