import json
import os

from req_helper import Signals


class DB(Signals):
    def __init__(self):
        Signals.__init__(self)
        self.db_url = self.notion_base_url + "/databases"
        self.page_id = os.getenv('PAGE_ID')
        self.id = self.get_db_id()

    def create_db(self):
        try:
            with open("db_schema.json", 'r') as db_schema:
                req_body = json.load(db_schema)
                req_body['parent']['page_id'] = self.page_id
                response = self.send_request(
                    endpoint_url=self.db_url, request_type="post", request_body=req_body
                )
                database_id = response['id'].replace('-', '')
                with open("db_id.txt", "w") as db_id:
                    db_id.write(database_id)
                return response
        except FileNotFoundError:
            raise SystemExit("Create a db_schema.json file at root level to proceed")

    def get_db(self, db_id):
        return self.send_request(endpoint_url=self.db_url+f"/{db_id}", request_type="get")

    def update_db(self, db_scehma, db_id):
        return self.send_request(endpoint_url=self.db_url+f"/{db_id}", request_type="patch", request_body=db_scehma)

    def get_db_id(self):
        try:
            with open('db_id.txt', 'r') as db_id:
                return db_id.read()
        except FileNotFoundError:
            return self.create_db()['id'].replace('-', '')
