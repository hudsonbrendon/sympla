from pysympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

print(sympla.checkin_by_ticket_id(event_id=config("EVENT_ID"), participant_id=config("PARTICIPANT_ID")))
