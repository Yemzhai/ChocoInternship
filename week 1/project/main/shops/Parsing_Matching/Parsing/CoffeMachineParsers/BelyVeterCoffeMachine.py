from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.BelyVeterBaseParser import get_start_bely_veter

url = 'https://shop.kz/kofevarki-kofemashiny/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1'
pages = 2

belyveter_coffee_machine = get_start_bely_veter(url, pages)

# for i in belyveter_coffee_machine:
#     print(i)
