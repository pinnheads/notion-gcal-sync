import os


class Filters:
    def __init__(self):
        self.page_id = os.getenv("PAGE_ID")

    def new_event(self):
        return {
            "property": "gcal_id",
            "rich_text": {
                "is_empty": True
            }
        }

    def update_event(self):
        return {
            "property": "Action",
            "select": {
                "equals": "Update 🩹"
            }
        }

    def delete_event(self):
        return {
            "property": "Action",
            "select": {
                "equals": "Delete 🗑"
            }
        }
