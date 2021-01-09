import Levenshtein as lev
from technodom_laptop import technodom_items
from sulpak_laptop import sulpak_items
from mechta_laptop import mechta_items
from bely_veter_laptop import bely_veter_items

def similarity(str1, str2):
    str1 = str.lower(str1).replace(' ', '')
    str2 = str.lower(str2).replace(' ', '')

    d = lev.distance(str1, str2)

    return 1 - (d / max(len(str1), len(str2)))


def find_similar(technodom_items, sulpak_items, mechta_items, bely_veter_items):
    result = []
    for i in range(len(technodom_items)):
        for j in range(len(sulpak_items)):
            for k in range(len(mechta_items)):
                for l in range(len(bely_veter_items)):
                    d = similarity(technodom_items[i][0][0], sulpak_items[j][0][0])
                    d = min(d, similarity(technodom_items[i][0][0], mechta_items[k][0][0]))
                    d = min(d, similarity(technodom_items[i][0][0], bely_veter_items[l][0][0]))

                    d = min(d, similarity(sulpak_items[j][0][0], mechta_items[k][0][0]))
                    d = min(d, similarity(sulpak_items[j][0][0], bely_veter_items[l][0][0]))

                    d = min(d, similarity(mechta_items[k][0][0], bely_veter_items[l][0][0]))
                    if d >= 0.05:    # если у нас процент схожести больше или равно 30% то эти строки схожи
                        result.append([technodom_items[i], sulpak_items[j], mechta_items[k], bely_veter_items[l]])
                        technodom_items.remove(technodom_items[i])
                        sulpak_items.remove(sulpak_items[j])
                        mechta_items.remove(mechta_items[k])
                        bely_veter_items.remove(bely_veter_items[l])
    return result





def get_list_with_price(items):
    for i in range(len(items)):
        items[i] = str.lower(items[i])
        price_start = items[i].find('price:')
        from_start = items[i].find('from:')
        price = items[i][price_start + 6:from_start].replace(' ', '') # 6 потому что в слове 'price:' 6 букв и да 'from:'
        new_price = ''
        for c in price:
            if (c >= '0' and c <= '9') or c == '.':
                new_price += c
        items[i] = [items[i][:price_start-1], new_price, items[i][from_start+6:]]
    return items

def merge_lists(technodom_items, sulpak_items, mechta_items, bely_veter_items):
    technodom_items = get_list_with_price(technodom_items)
    sulpak_items = get_list_with_price(sulpak_items)
    mechta_items = get_list_with_price(mechta_items)
    bely_veter_items = get_list_with_price(bely_veter_items)



    # print(bely_veter_items)
    # return 0

    return find_similar(
                technodom_items,
                sulpak_items,
                mechta_items,
                bely_veter_items
            )



ans = merge_lists(
    technodom_items,
    sulpak_items,
    mechta_items,
    bely_veter_items
)

for i in ans:
    for j in i:
        print(j)
        print('--------------------------------------')