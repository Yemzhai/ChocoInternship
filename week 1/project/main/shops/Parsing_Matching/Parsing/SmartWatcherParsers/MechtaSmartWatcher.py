from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.MechtaBaseParser import get_start_mechta

url = "https://www.mechta.kz/api/main/catalog_new/index.php?section=smart-chasy&page_num"
pages = 4

mechta_smart_whatches = get_start_mechta(url, pages)
# for i in mechta_smart_whatches:
#     print(i)