import os
from dotenv import load_dotenv


class Properties:
    def __init__(self):
        load_dotenv(dotenv_path=os.path.join(os.path.join(os.getcwd(), '.credentials'), '.env'))
        # API Related Headings
        self.notion_api_url = "https://api.notion.com/v1"
        self.notion_database_url = self.notion_api_url + "/databases"
        self.notion_page_url = self.notion_api_url + "/pages"
        self.auth_token = os.getenv("BEARER_TOKEN")
        self.notion_headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-02-22",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
        }
        self.notion_page_id = os.getenv('PAGE_ID')
        self.notion_db_id = ""
        self.db_name = "Personal Tasks"

        # DB QUERY FILTERS
        self.new_event_filter = {
            "filter": {
                "property": "gcal_id",
                "rich_text": {
                    "is_empty": True
                }
            }
        }
        self.update_event_filter = {
            "filter": {
                "property": "Action",
                "select": {
                    "equals": "Update"
                }
            }
        }
        self.delete_event_filter = {
            "filter": {
                "property": "Action",
                "select": {
                    "equals": "Delete"
                }
            }
        }

        # DB CREATION AND UPDATE SCHEMA
        self.db_parent_schema = {
            "type": "page_id",
            "page_id": self.notion_page_id,
        }
        self.db_title = [
            {
                "type": "text",
                "text": {
                    "content": self.db_name,
                    "link": None
                }
            }
        ]
        self.db_properties = {
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
            "Status": {
                "type": "select",
                "select": {
                    "options": [
                        {
                            "name": "Backlog",
                            "color": "brown"
                        },
                        {
                            "name": "To Do",
                            "color": "red"
                        },
                        {
                            "name": "In Progress",
                            "color": "orange"
                        },
                        {
                            "name": "Done",
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
                "type": "select",
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
                        },
                        {
                            "name": "CUSTOM",
                            "color": "yellow"
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
            },
            "Task Category": {
                "type": "select",
                "select": {
                    "options": [
                        {
                            "name": "Personal",
                            "color": "green"
                        },
                        {
                            "name": "Work",
                            "color": "red"
                        }
                    ]
                }
            }
        }
        self.create_db_schema = {"parent": self.db_parent_schema, "title": self.db_title, "properties":
            self.db_properties}
        self.update_db_schema = {"title": self.db_title, "properties": self.db_properties}
