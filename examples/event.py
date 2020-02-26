from decouple import config

from pysympla import Sympla


sympla = Sympla(token=config("TOKEN"))

print(sympla.events(id=config("EVENT_ID")))
