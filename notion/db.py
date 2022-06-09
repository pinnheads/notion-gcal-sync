import json
import os

from properties import Properties
from req_helper import Signals


class DB(Signals, Properties):
    def __init__(self):
        Signals.__init__(self)
        Properties.__init__(self)        
        self.id = self.notion_db_id = self.get_db_id()

    def create_db(self):
        response = self.send_request(
            endpoint_url=self.notion_database_url, request_type="post", request_body=self.create_db_schema
        )
        database_id = response['id'].replace('-', '')
        with open("db_id.txt", "w") as db_id:
            db_id.write(database_id)
        return response

    def get_db(self, db_id):
        return self.send_request(endpoint_url=self.notion_database_url+f"/{db_id}", request_type="get")

    def update_db(self, db_schema, db_id):
        return self.send_request(
            endpoint_url=self.notion_database_url+f"/{db_id}", request_type="patch", request_body=db_schema
        )

    def get_db_id(self):
        try:
            with open('db_id.txt', 'r') as db_id:
                return db_id.read()
        except FileNotFoundError:
            return self.create_db()['id'].replace('-', '')
