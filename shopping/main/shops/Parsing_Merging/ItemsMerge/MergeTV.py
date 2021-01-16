from .ActionsToMerge import ToMerge
from ..ItemsParse.TV import technodom_items, bely_veter_items, sulpak_items, mechta_items
from ..DB.PostToDB import post_to_db

tomerge = ToMerge()
tv = tomerge.merge_lists(
    technodom_items,
    sulpak_items,
    mechta_items,
    bely_veter_items
)

def post_tv():
    post_to_db(3, tv)

