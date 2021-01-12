from BelyVeterBaseParser import get_start_bely_veter
from MechtaBaseParser import get_start_mechta
from SulpakBaseParser import get_start_sulpak
from TechnodomBaseParser import get_start_technodom

url = 'https://shop.kz/kofevarki-kofemashiny/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1'
pages = 2
bely_veter_items = get_start_bely_veter(url, pages)


url = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=kofevarki-i-kofemashiny&page_num'
pages = 4
mechta_items = get_start_mechta(url, pages)


url = "https://www.sulpak.kz/f/kofemashiniy"
pages = 3
sulpak_items = get_start_sulpak(url, pages)


url = 'https://www.technodom.kz/aktobe/tehnika-dlja-kuhni/prigotovlenie-kofe/kofemashiny'
pages = 3
technodom_items = get_start_technodom(url, pages)
