from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.SulpakBaseParser import get_start_sulpak

url = "https://www.sulpak.kz/f/holodilniki"
pages = 4

sulpak_fridges = get_start_sulpak(url, pages)
# for i in sulpak_fridges:
#         print(i)