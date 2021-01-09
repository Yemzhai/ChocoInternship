from MechtaBaseParser import get_start_mechta

url = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=kofevarki-i-kofemashiny&page_num'
pages = 4

mechta_coffee_machine = get_start_mechta(url, pages)
# for i in mechta_coffe_machine:
#     print(i)