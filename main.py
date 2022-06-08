from gcsa.event import Event
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.join(os.getcwd(), '.credentials'), '.env'))

from req_helper import Signals
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
# Event color - 1-11
from beautiful_date import Jan, Apr, Jun

from notion.db import DB
from notion.notion import Notion


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
db.update_db(db_id=db.id, db_scehma={"title": [
        {
            "type": "text",
            "text": {
                "content": "Tasks - Updated 2",
                "link": None
            }
        }
    ],
    "properties": {
        "Title": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "Date": {
            "date": {}
        },
        "Reminders": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Email",
                        "color": "blue"
                    },
                    {
                        "name": "Popup",
                        "color": "green"
                    }
                ]
            }
        },
         "Action": {
            "type": "select",
            "select": {
                "options": [
                    {
                        "name": "Delete",
                        "color": "red"
                    },
                    {
                        "name": "Update",
                        "color": "green"
                    }
                ]
            }
        },
        "Frequency": {
            "type":"select",
            "select": {
                "options": [
                    {
                        "name": "DAILY",
                        "color": "red"
                    },
                    {
                        "name": "WEEKLY",
                        "color": "orange"
                    },
                    {
                        "name": "MONTHLY",
                        "color": "blue"
                    },
                    {
                        "name": "YEARLY",
                        "color": "purple"
                    },
                    {
                        "name": "SECONDLY",
                        "color": "pink"
                    },
                    {
                        "name": "HOURLY",
                        "color": "gray"
                    },
                    {
                        "name": "MINUTELY",
                        "color": "green"
                    }
                ]
            }
        },
        "Count": {
            "number": {}
        },
        "Interval": {
            "number": {}
        },
        "By Week Day": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "SU",
                        "color": "red"
                    },
                    {
                        "name": "MO",
                        "color": "orange"
                    },
                    {
                        "name": "TU",
                        "color": "blue"
                    },
                    {
                        "name": "WE",
                        "color": "purple"
                    },
                    {
                        "name": "TH",
                        "color": "pink"
                    },
                    {
                        "name": "FR",
                        "color": "gray"
                    },
                    {
                        "name": "SA",
                        "color": "green"
                    }
                ]
            }
        },
        "By Month": {
            "number": {}
        },
        "Minutes before Email Reminder": {
            "number": {}
        },
        "Minutes before Popup Reminder": {
            "number": {}
        },
        "notion_id": {
            "rich_text": {}
        },
        "gcal_id": {
            "rich_text": {}
        }
    }
})
