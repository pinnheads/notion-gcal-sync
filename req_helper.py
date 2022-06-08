import json
import os

import requests as req


def print_in_console(url, response, req_body=None):
    print(f"Endpoint Url -----> {url}")
    if req_body is None:
        print("Request Body ------> {}")
    else:
        print(f"Request Body ------> {req_body}")
    print(f"Response -----> {response}")


class Signals:
    """
    Sends different type of requests and provides json responses
    """
    def __init__(self):
        self.notion_base_url = "https://api.notion.com/v1"
        self.auth_token = os.getenv("BEARER_TOKEN")
        self.notion_headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-02-22",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
        }

    def send_request(self, endpoint_url, request_type, request_body=None):
        type_of_req = request_type.upper()
        if type_of_req == "GET":
            response = req.get(url=endpoint_url, headers=self.notion_headers)
            response.raise_for_status()
            result = response.json()
            print_in_console(url=endpoint_url, response=result, req_body=request_body)
            return result
        elif type_of_req == "POST":
            if request_body is None:
                raise ValueError("Request body is needed for a POST request")
            response = req.post(url=endpoint_url, headers=self.notion_headers, json=request_body)
            response.raise_for_status()
            result = response.json()
            print_in_console(url=endpoint_url, response=result, req_body=request_body)
            return result
        elif type_of_req == "PATCH":
            if request_body is None:
                raise ValueError("Request body is needed for a PATCH request")
            response = req.patch(url=endpoint_url, headers=self.notion_headers, json=request_body)
            response.raise_for_status()
            result = response.json()
            print_in_console(url=endpoint_url, response=result, req_body=request_body)
            return result
        else:
            raise ValueError("'request_type' only accepts GET, POST, PATCH as values")
