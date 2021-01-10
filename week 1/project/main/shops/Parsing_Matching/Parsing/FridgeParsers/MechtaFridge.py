from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.MechtaBaseParser import get_start_mechta

url = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=holodilniki&page_num'
pages = 3

mechta_fridges = get_start_mechta(url, pages)
# for i in mechta_fridges:
#     print(i)