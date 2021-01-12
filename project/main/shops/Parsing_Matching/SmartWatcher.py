from BelyVeterBaseParser import get_start_bely_veter
from MechtaBaseParser import get_start_mechta
from SulpakBaseParser import get_start_sulpak
from TechnodomBaseParser import get_start_technodom

url = 'https://shop.kz/smart-chasy/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1'
pages = 4
bely_veter_items = get_start_bely_veter(url, pages)


url = "https://www.mechta.kz/api/main/catalog_new/index.php?section=smart-chasy&page_num"
pages = 4
mechta_items = get_start_mechta(url, pages)


url = 'https://www.sulpak.kz/f/smart_chasiy'
pages = 4
sulpak_items = get_start_sulpak(url, pages)

url = "https://www.technodom.kz/aktobe/smartfony-i-gadzhety/gadzhety/smart-chasy"
pages = 4
technodom_items = get_start_technodom(url, pages)