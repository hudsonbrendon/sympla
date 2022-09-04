from decouple import config

from pysympla import Sympla

sympla = Sympla(token=config("TOKEN"))

print(sympla.orders_by_event(event_id=config("EVENT_ID")))
