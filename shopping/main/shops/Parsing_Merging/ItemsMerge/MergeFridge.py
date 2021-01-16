from .ActionsToMerge import ToMerge
from ..ItemsParse.Fridge import technodom_items, bely_veter_items, mechta_items, sulpak_items
from ..DB.PostToDB import post_to_db

tomerge = ToMerge()
fridges = tomerge.merge_lists(
    technodom_items,
    sulpak_items,
    mechta_items,
    bely_veter_items
)
def post_fridges():
    post_to_db(1, fridges)



