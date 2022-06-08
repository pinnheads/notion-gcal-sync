import os
import requests as req
import json

from notion.db import DB
from notion.filters import Filters


class Notion:
    def __init__(self):
        self.filters = Filters()
        self.db = DB()
        self.endpoint_url = "https://api.notion.com/v1/databases"
        self.auth_token = os.getenv("BEARER_TOKEN")
        self.headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-02-22",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
        }
        self.page_id = os.getenv("PAGE_ID")
        self.db_id = self.db.get_db_id()
        self.new_event_filter = {"filter": self.filters.new_event()}
        self.update_event_filter = {"filter": self.filters.update_event()}
        self.delete_event_filter = {"filter": self.filters.delete_event()}

    def query_db(self, event_filter):
        response = req.post(url=self.endpoint_url + f"/{self.db_id}/query", headers=self.headers,
                            json=event_filter)
        return response.json()

    def get_events(self, event_type: str):
        if event_type.lower() == "new":
            return self.query_db(event_filter=self.new_event_filter)
        elif event_type.lower() == "update":
            return self.query_db(event_filter=self.update_event_filter)
        elif event_type.lower() == "delete":
            return self.query_db(event_filter=self.delete_event_filter)
        else:
            raise ValueError

    def update_event(self, body):
        response = req.patch(url=self.endpoint_url)
