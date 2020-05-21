from pysympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

print(sympla.affiliates(event_id=config("EVENT_ID")))
