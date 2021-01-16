from .ActionsToMerge import ToMerge
from ..ItemsParse.SmartWatche import  technodom_items, bely_veter_items, mechta_items, sulpak_items
from ..DB.PostToDB import post_to_db

tomerge = ToMerge()
smart_watches = tomerge.merge_lists(
    technodom_items,
    sulpak_items,
    mechta_items,
    bely_veter_items
)
def post_smart_watches():
    post_to_db(2, smart_watches)

