from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.SulpakBaseParser import get_start_sulpak

url = 'https://www.sulpak.kz/f/led_oled_televizoriy'
pages = 4
sulpak_tv = get_start_sulpak(url, pages)

# for i in sulpak_tv:
#     print(i)
