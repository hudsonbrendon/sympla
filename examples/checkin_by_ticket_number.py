from pysympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

print(sympla.checkin_by_ticket_number(event_id=config("EVENT_ID"), ticket_number=config("TICKET_NUMBER")))
