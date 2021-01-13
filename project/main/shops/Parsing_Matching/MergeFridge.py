from ActionsToMerge import ToMerge

from Fridge import  technodom_items, bely_veter_items, mechta_items, sulpak_items

tomerge = ToMerge()
ans = tomerge.merge_lists(
    technodom_items,
    sulpak_items,
    mechta_items,
    bely_veter_items
)

