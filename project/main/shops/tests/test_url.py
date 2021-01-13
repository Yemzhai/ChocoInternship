from django.urls import resolve, reverse


class TestUrls:
    def test_detail_url(self):
        item_url = reverse('item_detail_url', kwargs={'pk': 1})
        category_url = reverse('category_detail_url', kwargs={'pk': 1})

        assert resolve(item_url).view_name == 'item_detail_url'
        assert resolve(category_url).view_name == 'category_detail_url'

    def test_all_url(self):
        item_url = reverse('items_url')
        category_url = reverse('categories_url')

        assert resolve(item_url).view_name == 'items_url'
        assert resolve(category_url).view_name == 'categories_url'
