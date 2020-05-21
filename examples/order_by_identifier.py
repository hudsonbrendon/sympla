from pysympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

print(sympla.orders(event_id=config("EVENT_ID"), order_id=config("ORDER_ID")))
