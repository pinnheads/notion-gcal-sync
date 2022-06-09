import os
import requests as req
import json

from notion.db import DB
from properties import Properties


class Notion(Properties, DB):
    def __init__(self):
        DB.__init__(self)
        Properties.__init__(self)

    def get_events(self, event_type: str):
        if event_type.lower() == "new":
            return self.query_db(event_filter=self.new_event_filter)
        elif event_type.lower() == "update":
            return self.query_db(event_filter=self.update_event_filter)
        elif event_type.lower() == "delete":
            return self.query_db(event_filter=self.delete_event_filter)
        else:
            raise ValueError

