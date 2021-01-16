from ...models import Price, Shop, Category, Item

def post_to_db(category_id, items):
    categories = ['Coffee Machine', 'Fridge', 'Smart Watch', 'TV']

    category, category_created = Category.objects.get_or_create(title=categories[category_id])
    for i in items:
        item, item_created = Item.objects.get_or_create(title=i[0][0], category=category)
        for j in i:
            shop, shop_created = Shop.objects.get_or_create(title=j[2])
            Price.objects.get_or_create(price=j[1], item=item, shop=shop, category=category)
