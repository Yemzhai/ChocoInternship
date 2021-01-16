from .ActionsToMerge import ToMerge
from ..ItemsParse.CoffeeMachine import technodom_items, bely_veter_items, mechta_items, sulpak_items
from ..DB.PostToDB import post_to_db
tomerge = ToMerge()

coffee_machines = tomerge.merge_lists(
    technodom_items,
    sulpak_items,
    bely_veter_items,
    mechta_items
)
def post_coffee_machines():
    post_to_db(0, coffee_machines)







