from project.main.shops.Parsing_Matching.Parsing.BaseOfParsers.TechnodomBaseParser import get_start_technodom
url = 'https://www.technodom.kz/aktobe/tv-audio-foto-video/televizory/led-televizory'
pages = 4

technodom_tv = get_start_technodom(url, pages)

# for i in technodom_tv:
#     print(i)




