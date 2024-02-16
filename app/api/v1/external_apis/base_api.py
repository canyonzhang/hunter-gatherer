
class BaseApi():
    def __init__(self) -> None:
        pass

    def make_request(self, url: str, method: str, headers: dict, params: dict, data: dict) -> dict:
        pass