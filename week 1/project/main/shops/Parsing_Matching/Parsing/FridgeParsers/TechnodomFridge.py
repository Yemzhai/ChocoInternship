from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.TechnodomBaseParser import get_start_technodom
url = "https://www.technodom.kz/aktobe/bytovaja-tehnika/hranenie-produktov-i-napitkov/holodil-niki"
pages = 3

technodom_fridges = get_start_technodom(url, pages)

# for i in technodom_fridges:
#         print(i)