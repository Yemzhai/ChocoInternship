import Levenshtein as lev

from BelyVeterFridge import belyveter_fridges as bely_veter_items
from TechnodomFridge import technodom_fridges as technodom_items
from MechtaFridge import mechta_fridges as mechta_items
from SulpakFridge import sulpak_fridges as sulpak_items


def similarity(str1, str2):
    str1 = str.lower(str1).replace(' ', '')
    str2 = str.lower(str2).replace(' ', '')

    d = lev.distance(str1, str2)

    return 1 - (d / max(len(str1), len(str2)))


def find_similar(technodom_items, sulpak_items, mechta_items, bely_veter_items):
    result = []
    used1 = {}
    used2 = {}
    used3 = {}
    used4 = {}

    for i in range(len(technodom_items)):
        if used1.get(i) is True: continue
        for j in range(len(sulpak_items)):
            if used2.get(j) is True: continue
            for k in range(len(mechta_items)):
                if used3.get(k) is True: continue
                for l in range(len(bely_veter_items)):
                    if used4.get(l) is True: continue

                    d = similarity(technodom_items[i][0], sulpak_items[j][0])
                    d = min(d, similarity(technodom_items[i][0], mechta_items[k][0]))
                    d = min(d, similarity(technodom_items[i][0], bely_veter_items[l][0]))

                    d = min(d, similarity(sulpak_items[j][0], mechta_items[k][0]))
                    d = min(d, similarity(sulpak_items[j][0], bely_veter_items[l][0]))

                    d = min(d, similarity(mechta_items[k][0], bely_veter_items[l][0]))
                    if d >= 0.3:  # если у нас процент схожести больше или равно 30% то эти строки схожи
                        result.append([technodom_items[i], sulpak_items[j], mechta_items[k], bely_veter_items[l]])
                        used1[i] = True
                        used2[j] = True
                        used3[k] = True
                        used4[l] = True
                        i += 1
                        j += 1
                        k += 1

    return result


def get_list_with_price(items):
    for i in range(len(items)):
        items[i] = str.lower(items[i])
        price_start = items[i].find('price:')
        from_start = items[i].find('from:')
        price = items[i][price_start + 6:from_start].replace(' ',
                                                             '')  # 6 потому что в слове 'price:' 6 букв и да 'from:'
        new_price = ''
        for c in price:
            if (c >= '0' and c <= '9') or c == '.':
                new_price += c
        items[i] = [items[i][:price_start - 1], new_price, items[i][from_start + 6:]]
    return items


def merge_lists(technodom_items, sulpak_items, mechta_items, bely_veter_items):
    technodom_items = get_list_with_price(technodom_items)
    sulpak_items = get_list_with_price(sulpak_items)
    mechta_items = get_list_with_price(mechta_items)
    bely_veter_items = get_list_with_price(bely_veter_items)

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