from datetime import date
import os
from gcsa.google_calendar import GoogleCalendar

from gcal import TaskToEvent
from notion.db import DB
from notion.notion import Notion, create_event_from_tasks
from notion.page import Page

page = Page()
notion = Notion()

credentials_path = os.path.join(
    os.path.join(os.getcwd(), ".credentials"), "client_secrets.json"
)
calendar = GoogleCalendar("utsavdeep01@gmail.com", credentials_path=credentials_path)


def create_event_gcal(query_result):
    for data in query_result:
        # create dictionary from notion data as a new task
        new_task = create_event_from_tasks(data)
        # convert dictionary to an Event Object from gcsa
        new_event = TaskToEvent(new_task)
        # create event in gcal
        event = new_event.create_event()
        if event is not None:
            # add event to calendar
            response = calendar.add_event(event)
            # update notion_id and gcal_id field in notion
            page.update_gcal_notion_id(
                id=new_task.get("_id"),
                gcal_id=response.id,
                notion_id=new_task.get("_id"),
            )


def get_event_gcal(event_id):
    return calendar.get_event(event_id)


def update_event_gcal(query_result):
    for data in query_result:
        # create dictionary from notion data as a new task
        new_task = create_event_from_tasks(data)
        print(new_task)
        # convert dictionary to an Event Object from gcsa
        new_event = TaskToEvent(new_task)
        # create event in gcal
        event = new_event.create_event()
        if event is not None:
            # add event to calendar
            calendar.update_event(event=event)
            page.update_action(id=new_task.get("_id"))


def delete_event_gcal(query_result):
    for data in query_result:
        # create dictionary from notion data as a new task
        new_task = create_event_from_tasks(data)
        # convert dictionary to an Event Object from gcsa
        new_event = TaskToEvent(new_task)
        # create event in gcal
        event = new_event.create_event()
        if event is not None:
            calendar.delete_event(event=event)
            page.delete_page(id=new_task.get("_id"))


def update_notion():
    # get today's events from google calendar
    today = date.today()
    todays_events = calendar.get_events(
        time_min=today, time_max=today, order_by="startTime", single_events=True
    )

    db_id = notion.get_db_id()

    # update notion tasks with respective dates
    for event in todays_events:
        if event.description:
            pg_id = event.description.split("\n")[0].split(":")[1].replace(" ", "")
            req_body = {
                "properties": {
                    "Last Occurence": {
                        "date": {
                            "start": str(event.start).replace(" ", "T"),
                            "end": str(event.end).replace(" ", "T"),
                        }
                    }
                }
            }
            page.update_page(id=pg_id, req_body=req_body)
        else:
            req_body = {
                "parent": {"database_id": db_id},
                "properties": {
                    "Title": {"title": [{"text": {"content": event.summary}}]},
                    "Status": {"select": {"name": "Backlog"}},
                    "Date": {
                        "date": {
                            "start": event.start.strftime(
                                "%Y-%m-%dT%H:%M:%S.000+05:30"
                            ),
                            "end": event.end.strftime("%Y-%m-%dT%H:%M:%S.000+05:30"),
                        }
                    },
                    "Action": {"select": {"name": "Update"}},
                    "Reminders": {"multi_select": [{"name": "Popup"}]},
                    "Minutes before Popup Reminder": {"number": 10},
                },
            }
            response = page.create_page(req_body=req_body)
            page_id = response.get("id")
            page.update_gcal_notion_id(id=page_id, notion_id=page_id, gcal_id=event.id)


if __name__ == "__main__":
    # Update Notion
    update_notion()

    # get new events
    new_events = notion.get_events("new")["results"]
    create_event_gcal(query_result=new_events)

    # get events to be updates
    update_events = notion.get_events("update")["results"]
    update_event_gcal(query_result=update_events)

    # get events to delete
    delete_events = notion.get_events("delete")["results"]
    delete_event_gcal(query_result=delete_events)

    # notion.update_db(db_schema=notion.update_db_schema, db_id=notion.get_db_id())
