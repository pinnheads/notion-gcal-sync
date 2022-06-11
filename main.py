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


new_events = notion.get_events(event_type="new")
for data in new_events.get('results'):
    new_task = create_event_from_tasks(data)
    print(new_task)
    new_event = TaskToEvent(new_task)
    event = new_event.create_event()
    response = calendar.add_event(event)
    print(response.id)