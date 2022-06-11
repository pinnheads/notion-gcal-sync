from notion.db import DB
from properties import Properties


def get_property_value(property_type, task_property):
    match property_type:
        case "rich_text":
            try:
                return [data.get('text').get('content') for data in task_property.get('rich_text')]
            except Exception:
                return None

        case "number":
            try:
                return int(task_property.get('number'))
            except Exception:
                return None

        case "multi_select":
            try:
                return [data.get('name') for data in task_property.get('multi_select')]
            except Exception:
                return None

        case "select":
            try:
                return task_property.get('select').get('name')
            except Exception:
                return None

        case "title":
            try:
                return task_property.get("title")[0].get('text').get('content')
            except Exception:
                return "No Title"

        case "date":
            try:
                date = task_property.get("date")
                return {"start": date.get("start"), "end": date.get("end")}
            except Exception:
                return None

        case "checkbox":
            try:
                return task_property.get("checkbox")
            except Exception:
                return False


def create_event_from_tasks(task):
    properties = task.get('properties')
    event = {'_id': task.get('id'), 'notion_url': task.get('url')}
    for task_property in properties:
        event[task_property.lower().replace(" ", "_")] = get_property_value(
            property_type=properties.get(task_property).get('type'), task_property=properties.get(task_property))
    return event


class Notion(DB):
    def __init__(self):
        DB.__init__(self)

    def get_events(self, event_type: str):
        if event_type.lower() == "new":
            return self.query_db(query_filter=self.new_event_filter, db_id=self.notion_db_id)
        elif event_type.lower() == "update":
            return self.query_db(query_filter=self.update_event_filter, db_id=self.notion_db_id)
        elif event_type.lower() == "delete":
            return self.query_db(query_filter=self.delete_event_filter, db_id=self.notion_db_id)
        else:
            raise ValueError
