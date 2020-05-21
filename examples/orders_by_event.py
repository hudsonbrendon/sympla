from pysympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

print(sympla.orders_by_event(event_id=config("EVENT_ID")))
