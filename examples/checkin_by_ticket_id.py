from decouple import config

from pysympla import Sympla

sympla = Sympla(token=config("TOKEN"))

print(
    sympla.checkin_by_ticket_id(
        event_id=config("EVENT_ID"), participant_id=config("PARTICIPANT_ID")
    )
)
