from project.main.shops.Parsing_Matching.Matching import MergeCoffeeMachine, \
    MergeTV, \
    MergeFridge, \
    MergeSmartWatches
from celery import shared_task
import psycopg2

@shared_task()
def push():
    try:
        conn = psycopg2.connect(
            user='postgres',
            database='shopsDemo',
            password='123456789i',
            host='localhost',
            port='5432'
        )

        cursor = conn.cursor()

        # MergeCoffeeMachine.main(conn, cursor)
        # MergeTV.main(conn, cursor)
        # MergeFridge.main(conn, cursor)
        # MergeSmartWatches.main(conn, cursor)

        print('OK')
    except:
        print('Something was wrong')
