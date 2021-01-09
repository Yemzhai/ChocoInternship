from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class SulpakParser(object):
    def __init__(self, driver, sulpak_items, url, pages):
        self.driver = driver
        self.sulpak_items = sulpak_items
        self.url = url
        self.pages = pages

    def parse(self):
        delay = 5
        for page in range(1, self.pages): #13
            item_from = 'sulpak'
            try:
                self.driver.get(f'{self.url}?page={page}')
                try:
                    WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'location-window-button')))
                    btn_city = self.driver.find_element_by_class_name('location-window-button')
                    btn_city.click()
                except:
                    pass
                WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'tile-container')))

                print(page, "- Sulpak page is ready!")

                product_cards = self.driver.find_elements_by_class_name('tile-container')
                for item in product_cards:
                    name = item.find_element_by_class_name('title').text
                    availability = item.find_element_by_class_name('availability').text
                    if(availability == 'Есть в наличии'):
                        price = item.find_element_by_class_name('price').text
                    else:
                        price = None
                    information = str(str(name) + ' price: ' + str(price) + ' from: ' + item_from)  # convert item's informatoins to string and store
                    self.sulpak_items.append(information)  # push to list

            except TimeoutException:
                print("Loading took too much time!")
        self.driver.close()


def get_start_sulpak(url, pages):
    driver = webdriver.Chrome()
    sulpak_items = []
    sulpak_parser = SulpakParser(driver, sulpak_items, url, pages)
    sulpak_parser.parse()
    return sulpak_items

    # for i in sulpak_items:
    #     print(i)
