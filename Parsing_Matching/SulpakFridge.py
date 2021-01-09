from SulpakBaseParser import get_start_sulpak

url = "https://www.sulpak.kz/f/holodilniki"
pages = 5

sulpak_fridges = get_start_sulpak(url, pages)
# for i in sulpak_fridges:
#         print(i)