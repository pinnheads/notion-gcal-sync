# from gcsa.event import Event
# import os
#
#
# from req_helper import Signals
# from gcsa.google_calendar import GoogleCalendar
# from gcsa.recurrence import Recurrence, DAILY, SU, SA
# # Event color - 1-11
# from beautiful_date import Jan, Apr, Jun

from notion.db import DB
# from notion.notion import Notion


# credentials_path = os.path.join(os.path.join(os.getcwd(), '.credentials'), 'client_secrets.json')
# calendar = GoogleCalendar('utsavdeep01@gmail.com', credentials_path=credentials_path)
# event = Event(
#     'Breakfast-2',
#     start=(7 / Jun / 2022)[8:00],
#     color_id="4",
#     minutes_before_email_reminder=50
# )
#
# response = calendar.add_event(event)
# print(response.id)

db = DB()
# db.update_db(db_id=db.id, db_schema=)
