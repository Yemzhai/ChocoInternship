from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .Parsing_Merging.ItemsMerge.MergeCoffeeMachine import post_coffee_machines
from .Parsing_Merging.ItemsMerge.MergeFridge import post_fridges
from .Parsing_Merging.ItemsMerge.MergeSmartWatches import post_smart_watches
from .Parsing_Merging.ItemsMerge.MergeTV import post_tv

@shared_task
def add_to_db():
    try:
        post_coffee_machines()
        post_fridges()
        post_smart_watches()
        post_tv()
    except Exception as e:
        print("Exc:", e)
