from decouple import config

from pysympla import Sympla

sympla = Sympla(token=config("TOKEN"))

print(sympla.affiliates(event_id=config("EVENT_ID")))
