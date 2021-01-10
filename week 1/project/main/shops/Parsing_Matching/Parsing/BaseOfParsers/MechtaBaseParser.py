import requests
import json

class MechtaParser(object):
    def __init__(self, mechta_items, url, pages):
        self.mechta_items = mechta_items
        self.url = url
        self.pages = pages

    def parse(self):
        item_from = 'mechta'
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
        }
        for page in range (1, self.pages):
            print(page, "- Mechta page is ready!")
            URL = f"{self.url}={page}&catalog=true&page_element_count=18"
            req = requests.get(URL, headers=HEADERS)
            JSON = json.loads(req.text)
            i = 0
            try:
                while(i <= 100):
                    name = JSON['data']['ITEMS'][i]['NAME']
                    price = JSON['data']['ITEMS'][i]['PRICE']['PRICE']
                    information = str(name + ' price: ' + str(price) + ' from: ' + item_from)  # convert item's informatoins to string and store
                    self.mechta_items.append(information)  # push to list
                    i += 1
            except:
                pass

def get_start_mechta(url, pages):
    mechta_items = []
    mechta_parser = MechtaParser(mechta_items, url, pages)
    mechta_parser.parse()
    return mechta_items
    # for i in mechta_items:
    #     print(i)