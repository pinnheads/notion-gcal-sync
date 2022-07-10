from properties import Properties
from req_helper import Signals


class Page(Signals, Properties):
    def __init__(self):
        Signals.__init__(self)
        Properties.__init__(self)

    def get_page(self, id: str):
        return self.send_request(
            endpoint_url=self.notion_page_url + f"/{id}", request_type="get"
        )

    def update_page(self, id, req_body):
        return self.send_request(
            endpoint_url=self.notion_page_url + f"/{id}",
            request_type="patch",
            request_body=req_body,
        )

    def delete_page(self, id):
        delete_body = {"archived": True}
        return self.send_request(
            endpoint_url=self.notion_page_url + f"/{id}",
            request_type="patch",
            request_body=delete_body,
        )

    def update_gcal_notion_id(self, id, notion_id=None, gcal_id=None):
        req_body = {
            "properties": {
                "notion_id": {
                    "rich_text": [{"type": "text", "text": {"content": notion_id}}]
                },
                "gcal_id": {
                    "rich_text": [{"type": "text", "text": {"content": gcal_id}}]
                },
            }
        }
        return self.send_request(
            endpoint_url=self.notion_page_url + f"/{id}",
            request_type="patch",
            request_body=req_body,
        )

    def update_action(self, id, action_to_set=None):
        if action_to_set is not None:
            req_body = {"properties": {"Action": {"select": {"name": action_to_set}}}}
        else:
            req_body = {"properties": {"Action": {"select": None}}}
        return self.send_request(
            endpoint_url=self.notion_page_url + f"/{id}",
            request_type="patch",
            request_body=req_body,
        )

    def create_page(self, req_body):
        return self.send_request(
            endpoint_url=self.notion_page_url,
            request_type="post",
            request_body=req_body,
        )
