import os
from gcsa.google_calendar import GoogleCalendar

from gcal import TaskToEvent
from notion.db import DB
from notion.notion import Notion, create_event_from_tasks
from notion.page import Page

db = DB()
page = Page()
notion = Notion()

credentials_path = os.path.join(os.path.join(os.getcwd(), '.credentials'), 'client_secrets.json')
calendar = GoogleCalendar('utsavdeep01@gmail.com', credentials_path=credentials_path)
# event = Event(
#     'Breakfast-2',
#     start=(7 / Jun / 2022)[8:00],
#     color_id="4",
#     minutes_before_email_reminder=50
# )
#
# response = calendar.add_event(event)
# print(response.id)


new_events = notion.get_events(event_type="new")
for data in new_events.get('results'):
    new_task = create_event_from_tasks(data)
    new_event = TaskToEvent(new_task)
    event = new_event.create_event()
    response = calendar.add_event(event)
