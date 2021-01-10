from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.BelyVeterBaseParser import get_start_bely_veter

url = 'https://shop.kz/kholodilniki/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1'
pages = 2

belyveter_fridges = get_start_bely_veter(url, pages)

# for i in belyveter_fridges:
#     print(i)