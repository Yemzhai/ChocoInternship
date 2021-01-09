from SulpakBaseParser import get_start_sulpak

url = 'https://www.sulpak.kz/f/smart_chasiy'
pages = 5
sulpak_smart_whatches = get_start_sulpak(url, pages)

for i in sulpak_smart_whatches:
    print(i)

