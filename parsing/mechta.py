import requests
from bs4 import BeautifulSoup
import json
URL = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=noutbuki&page_num=1&catalog=true&page_element_count=18'

def get_data(url):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
    }
    # req = requests.get(url, headers=HEADERS)

    # with open('MechtaKZ.json', 'w') as file:
    #     file.write(req.text)
    with open('MechtaKZ.json') as json_file:
        data = json.load(json_file)
        print(data['data']['ITEMS'][0]['ID'])
        print(data['data']['ITEMS'][0]['NAME'])
        print(data['data']['ITEMS'][0]['BONUS'])



get_data(URL)