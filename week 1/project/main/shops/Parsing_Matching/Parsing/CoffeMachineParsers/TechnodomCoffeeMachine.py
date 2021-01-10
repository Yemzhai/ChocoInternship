from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.TechnodomBaseParser import get_start_technodom

url = 'https://www.technodom.kz/aktobe/tehnika-dlja-kuhni/prigotovlenie-kofe/kofemashiny'
pages = 3
technodom_coffee_machine = get_start_technodom(url, pages)

# for i in technodom_coffe_machine:
#     print(i)