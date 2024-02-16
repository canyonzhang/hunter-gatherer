
from app.api.v1.external_apis.base_api import BaseApi


class SquareSpaceAPI(BaseApi):
    def __init__(self, api_key):
        self.api_key = api_key

    def make_request(self, url: str, method: str, headers: dict, params: dict, data: dict) -> dict:
        pass