import Levenshtein as lev

class ToMerge():
    # считает возвращает процент схожести, алгоритм левенштейна
    def similarity(self ,str1, str2):
        str1 = str.lower(str1).replace(' ', '')
        str2 = str.lower(str2).replace(' ', '')
        d = lev.distance(str1, str2)
        return 1 - (d / max(len(str1), len(str2)))

    #берет 4 массива с товарами и мерджит если и процент схожести 30% или выше
    def find_similar(self, technodom_items, sulpak_items, mechta_items, bely_veter_items):
        result = []
        used1 = {}
        used2 = {}
        used3 = {}
        used4 = {}

        for i in range(len(technodom_items)):
            if used1.get(i) is True: continue
            to_break = False
            for j in range(len(sulpak_items)):
                if used2.get(j) is True: continue
                for k in range(len(mechta_items)):
                    if used3.get(k) is True: continue
                    for l in range(len(bely_veter_items)):
                        if used4.get(l) is True: continue

                        d = self.similarity(technodom_items[i][0], sulpak_items[j][0])
                        d = min(d, self.similarity(technodom_items[i][0], mechta_items[k][0]))
                        d = min(d, self.similarity(technodom_items[i][0], bely_veter_items[l][0]))

                        d = min(d, self.similarity(sulpak_items[j][0], mechta_items[k][0]))
                        d = min(d, self.similarity(sulpak_items[j][0], bely_veter_items[l][0]))

                        d = min(d, self.similarity(mechta_items[k][0], bely_veter_items[l][0]))
                        if d >= 0.3:  # если у нас процент схожести больше или равно 30% то эти строки схожи
                            result.append([technodom_items[i], sulpak_items[j], mechta_items[k], bely_veter_items[l]])
                            used1[i] = True
                            used2[j] = True
                            used3[k] = True
                            used4[l] = True
                            to_break = True
                            break

                    if to_break: break
                if to_break: break

        return result

    # приходит массив стрингов а функция убирает все ненужные слова и ретурнит массив стрингов
    # i.e. ['Iphone X price: 250.000тг from: sulpak'] => ['iphone x', '250.000', 'sulpal']
    def get_list_with_price(self, items):
        for i in range(len(items)):
            items[i] = str.lower(items[i])
            price_start = items[i].find('price:')
            from_start = items[i].find('from:')
            price = items[i][price_start + 6:from_start].replace(' ','')
            new_price = ''
            for c in price:
                if (c >= '0' and c <= '9') or c == '.':
                    new_price += c
            if new_price != '':
                items[i] = [items[i][:price_start - 1], new_price, items[i][from_start + 6:]]
        return items

    # фукция которая принимает массив строк и заменяет их на измененный и отправляет на сравнение
    def merge_lists(self, items_1, items_2, items_3, items_4):
        items_1 = self.get_list_with_price(items_1)
        items_2 = self.get_list_with_price(items_2)
        items_3 = self.get_list_with_price(items_3)
        items_4 = self.get_list_with_price(items_4)

        return self.find_similar(
            items_1,
            items_2,
            items_3,
            items_4
        )