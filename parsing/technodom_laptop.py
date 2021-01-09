from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class TechnodomParser(object):
    def __init__(self, driver, technodom_items):
        self.driver = driver
        self.technodom_items = technodom_items
    def parse(self):
        delay = 5
        for page in range(1, 2): #12

            item_from = 'technodom'

            self.driver.get('https://www.technodom.kz/aktobe/noutbuki-i-komp-jutery/noutbuki-i-aksessuary/noutbuki?page={}'.format(page))
            try:
                try:
                    WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'ButtonNext__Text_Size-L')))
                    btn_city = self.driver.find_element_by_class_name('ButtonNext__Text_Size-L')
                    btn_city.click()
                except:
                    pass

                WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'ProductCard')))
                print(page, "- Technodom page is ready!")

                product_cards = self.driver.find_elements_by_class_name('ProductCard')
                for item in product_cards:
                    name = item.find_element_by_tag_name('h4').text
                    if len(name) != 0:
                        price = item.find_element_by_tag_name('data').text
                        information = str(name + ' price: ' + price + ' from: ' + item_from) #convert item's informatoins to string and store

                        self.technodom_items.append(information) #push to list
            except TimeoutException:
                print("Loading took too much time!")
        self.driver.close()

        

driver = webdriver.Chrome()
technodom_items = []
technodom_parser = TechnodomParser(driver, technodom_items)
technodom_parser.parse()

# for i in technodom_items:
#     print(i)

