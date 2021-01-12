from BelyVeterBaseParser import get_start_bely_veter
from MechtaBaseParser import get_start_mechta
from SulpakBaseParser import get_start_sulpak
from TechnodomBaseParser import get_start_technodom

url = 'https://shop.kz/kholodilniki/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1'
pages = 2
bely_veter_items = get_start_bely_veter(url, pages)


url = 'https://www.mechta.kz/api/main/catalog_new/index.php?section=holodilniki&page_num'
pages = 3
mechta_items = get_start_mechta(url, pages)


url = "https://www.sulpak.kz/f/holodilniki"
pages = 4
sulpak_items = get_start_sulpak(url, pages)

url = "https://www.technodom.kz/aktobe/bytovaja-tehnika/hranenie-produktov-i-napitkov/holodil-niki"
pages = 3
technodom_items = get_start_technodom(url, pages)