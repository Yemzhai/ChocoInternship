from ..Parsing_Matching.ActionsToMerge import ToMerge
tomerge = ToMerge()


class TestMerge:

    def test_merge_lists(self):
        assert tomerge.merge_lists(
                                    ['Macbook 2020 13inch M1 8gb 256gb price: 550000tg from: Technodom'],
                                    ['MACBOOK Ноутбук 13/8gb/256gb 2020 Price: 500000тг From: Mechta'],
                                    ['Macbook 13inch 2020 M1/8gb/256 price: 590000 from: SULPAK'],
                                    ['macbook 2020 13 8gb/M1/256 Price: 590000т from: ALSER']
                                   ) == [[
                                            ['macbook 2020 13inch m1 8gb 256gb', '550000', 'technodom'],
                                            ['macbook ноутбук 13/8gb/256gb 2020', '500000', 'mechta'],
                                            ['macbook 13inch 2020 m1/8gb/256', '590000', 'sulpak'],
                                            ['macbook 2020 13 8gb/m1/256', '590000', 'alser']
                                       ]]

        assert tomerge.merge_lists(
                                       ['Iphone X 2018 128gb price: 350000 from: Technodom'],
                                       ['SAMSUNG S20 price: 400000 from: Mechta'],
                                       ['Xiaomi Redmi Note price: 150000 From: Sulpak'],
                                       ['Huawei Mate 20 PRO price: 510000 from: Bely Veter']
                                   ) == []

    def test_get_list_with_price(self):
        assert tomerge.get_list_with_price(['Macbook 13/M1 2020 Price: 550000 from: Technodom']) == [['macbook 13/m1 2020',
                                                                                                     '550000',
                                                                                                     'technodom'
                                                                                                     ]]
        assert tomerge.get_list_with_price(
                                            [   'LG TV 4k price: 999999 from: Mechta',
                                                'TV Panasonic PRICE: 1543432 FROM: ALSER',
                                                'Airpods priCe: 20000 frOM: SulPAk'
                                             ]
                                            ) == \
                                            [
                                             ['lg tv 4k', '999999', 'mechta'],
                                             ['tv panasonic', '1543432', 'alser'],
                                             ['airpods', '20000', 'sulpak']
                                            ]

    def test_similarity(self):
        assert tomerge.similarity('qwerty', 'qwerty') == 1
        assert tomerge.similarity('qwerty', 'ytrewq') == 0


    def test_find_similar(self):
        assert tomerge.find_similar([['macbook 2020 13inch m1 8gb 256gb', '550000', 'technodom']],
                                    [['macbook ноутбук 13/8gb/256gb 2020', '500000', 'mechta']],
                                    [['macbook 13inch 2020 m1/8gb/256', '590000', 'sulpak']],
                                    [['macbook 2020 13 8gb/m1/256', '590000', 'alser']]
                                    ) == [[
                                            ['macbook 2020 13inch m1 8gb 256gb', '550000', 'technodom'],
                                            ['macbook ноутбук 13/8gb/256gb 2020', '500000', 'mechta'],
                                            ['macbook 13inch 2020 m1/8gb/256', '590000', 'sulpak'],
                                            ['macbook 2020 13 8gb/m1/256', '590000', 'alser']
                                         ]]

        assert tomerge.find_similar([['iphone x 2018 128gb', '350000', 'technodom']],
                                    [['samsung s20', '400000', 'mechta']],
                                    [['xiaomi redmi note', '150000', 'sulpak']],
                                    [['huawei mate 20 pro', '510000', 'bely veter']]
                                    ) == []
