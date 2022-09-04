from decouple import config

from pysympla import Sympla

sympla = Sympla(token=config("TOKEN"))

print(
    sympla.participant_by_ticket_number(
        event_id=config("EVENT_ID"), ticket_number=config("TICKET_NUMBER")
    )
)
