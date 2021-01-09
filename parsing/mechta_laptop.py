import requests
import json

mechta_items = []
class MechtaParser():
    def __init__(self, mechta_items):
        self.mechta_items = mechta_items

    def parse(self):
        item_from = 'mechta'
        HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36'
        }
        for page in range (1, 2):
            print(page, "- Mechta page is ready!")
            URL = "https://www.mechta.kz/api/main/catalog_new/index.php?section=noutbuki&page_num={}&catalog=true&page_element_count=18".format(page)
            req = requests.get(URL, headers=HEADERS)
            JSON = json.loads(req.text)
            i = 0
            try:
                while(i <= 100):
                    name = JSON['data']['ITEMS'][i]['NAME']
                    price = JSON['data']['ITEMS'][i]['PRICE']['PRICE']
                    information = str(name + ' price: ' + str(price) + ' from: ' + item_from)  # convert item's informatoins to string and store
                    self.mechta_items.append(information)  # push to list
                    i+=1
            except:
                pass


mechta_parser = MechtaParser(mechta_items)
mechta_parser.parse()

# for i in mechta_items:
#     print(i)