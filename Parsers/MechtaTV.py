from MechtaBaseParser import get_start_mechta

url = "https://www.mechta.kz/api/main/catalog_new/index.php?section=televizory&page_num"
pages = 4

mechta_tv = get_start_mechta(url, pages)
# for i in mechta_tv:
#     print(i)