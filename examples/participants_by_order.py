from decouple import config

from pysympla import Sympla

sympla = Sympla(token=config("TOKEN"))

print(
    sympla.participants_by_order(
        event_id=config("EVENT_ID"), order_id=config("ORDER_ID")
    )
)
