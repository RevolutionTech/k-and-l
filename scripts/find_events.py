import datetime
import os

from gcsa.google_calendar import GoogleCalendar


GOOGLE_API_CREDENTIALS_PATH = os.path.join("scratch", "google-api-credentials.json")


def clean_email(email: str) -> str:
    username, domain = email.split("@")
    username = username.split("+")[0]
    username = username.replace(".", "")
    cleaned_email = f"{username}@{domain}".lower()
    return cleaned_email

def find_events(events, attendees):
    num_events = 0
    first_event = None
    last_event = None

    for event in events:
        event_attendees = {clean_email(attendee.email) for attendee in event.attendees}
        if attendees.issubset(event_attendees):
            num_events += 1
            if first_event is None:
                first_event = event
            last_event = event

    return num_events, first_event, last_event

def runscript():
    date_string_start = input("Start date: ")
    first_attendee = input("First attendee: ")
    second_attendee = input("Second attendee: ")
    dt_start = datetime.datetime.strptime(date_string_start, "%Y-%m-%d").date()
    dt_today = datetime.datetime.now().date()
    print(f"Searching events between {dt_start} - {dt_today} for attendees {first_attendee}, {second_attendee}.")

    calendar = GoogleCalendar(credentials_path=GOOGLE_API_CREDENTIALS_PATH)
    events = calendar.get_events(dt_start, dt_today, single_events=True, order_by="startTime")
    attendees = {clean_email(attendee) for attendee in (first_attendee, second_attendee)}
    num_events, first_event, last_event = find_events(events, attendees)
    print(
        f"The attendees {first_attendee}, {second_attendee} have been invited "
        f"to a total of {num_events} events between {dt_start} - {dt_today}. "
        f"The first event was {first_event}. The last event was {last_event}."
    )

if __name__ == "__main__":
    runscript()
