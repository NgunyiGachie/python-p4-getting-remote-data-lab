import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = self.url
        response = requests.get(URL)
        return response.content

    def load_json(self):
        response_list = []
        responses = json.loads(self.get_response_body())
        for response in responses:
            response_list.append(response)
        return response_list
