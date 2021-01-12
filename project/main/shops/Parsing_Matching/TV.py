from TechnodomBaseParser import get_start_technodom
from BelyVeterBaseParser import get_start_bely_veter
from SulpakBaseParser import get_start_sulpak
from MechtaBaseParser import get_start_mechta


url = 'https://www.technodom.kz/aktobe/tv-audio-foto-video/televizory/led-televizory'
pages = 4
technodom_items = get_start_technodom(url, pages)


url = 'https://shop.kz/televizory/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1'
pages = 4
bely_veter_items = get_start_bely_veter(url, pages)


url = 'https://www.sulpak.kz/f/led_oled_televizoriy'
pages = 4
sulpak_items = get_start_sulpak(url, pages)


url = "https://www.mechta.kz/api/main/catalog_new/index.php?section=televizory&page_num"
pages = 4
mechta_items = get_start_mechta(url, pages)


