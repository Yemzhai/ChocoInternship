from SulpakBaseParser import get_start_sulpak

url = "https://www.sulpak.kz/f/kofemashiniy"
pages = 3

sulpak_coffee_machine = get_start_sulpak(url, pages)

# for i in sulpak_coffe_machine:
#     print(i)