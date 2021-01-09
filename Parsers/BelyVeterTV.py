from BelyVeterBaseParser import get_start_bely_veter

url = 'https://shop.kz/televizory/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1'
pages = 4

belyveter_tv = get_start_bely_veter(url, pages)

# for i in belyveter_tv:
#     print(i)