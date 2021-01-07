import requests
from bs4 import BeautifulSoup
import json
URL = "https://www.technodom.kz/graphql?hash=2228946361&_currentPage_0=9&_pageSize_0=24&_filter_0={category_url_path:{eq:noutbuki-i-komp-jutery/noutbuki-i-aksessuary/noutbuki}}&_sort_0={score:DESC}&_attributes_0=sticker,brands&_isNightSalesActive_0=0"

def get_data(url):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36',
        
    }
    req = requests.get(url, headers=HEADERS)
    print(req)

    # with open('TechnoDom.json', 'w') as file:
    #     file.write(req.text)
    # with open('TechnoDom.json') as json_file:
    #     data = json.load(json_file)
    #     print(data['data']['products']['items'][0]['seo_name'])
    #     # print(data['data']['products']['items'][10]['special_price'])
       


get_data(URL)