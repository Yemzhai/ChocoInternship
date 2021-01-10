from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.TechnodomBaseParser import get_start_technodom
url = "https://www.technodom.kz/aktobe/smartfony-i-gadzhety/gadzhety/smart-chasy"
pages = 4

technodom_smart_whatches = get_start_technodom(url, pages)

# for i in technodom_smart_whatches:
#     print(i)

