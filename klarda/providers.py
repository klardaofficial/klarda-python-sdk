from __future__ import annotations

from typing import Any, Optional, Union

from eth_typing import URI
from typing_extensions import Protocol
from klarda.exceptions import APIError
import requests

class KlardaProvider():
    def __init__(
        self,
        api_key: str,
        endpoint_uri: str = None,
    ) -> None:
        self.endpoint_uri = endpoint_uri or "https://api.klarda.com/api/v1/"
        self.api_key = api_key

    def make_request(self, method_url: str, params: Optional[Any], reply: Optional[Any]) -> Optional[Any]:
        if not isinstance(params, dict):
            params = params.to_dict()
        params["api_key"] = self.api_key
        response = requests.get(self.endpoint_uri + method_url, params=params).json()
        reply = [reply.from_dict(**item) for item in response["data"]]
        if response.get("error"):
            raise APIError(response["error"])
        if len(response["data"]) == 0:
            raise APIError("returned no result")
        return reply
    
    def make_request_with_total(self, method_url: str, params: Optional[Any], reply: Optional[Any]) -> Optional[Any]:
        if not isinstance(params, dict):
            params = params.to_dict()
        params["api_key"] = self.api_key
        response = requests.get(self.endpoint_uri + method_url, params=params).json()
        reply = [reply.from_dict(**item) for item in response["data"]["result"]]
        if response.get("error"):
            raise APIError(response["error"])
        if len(response["data"]["result"]) == 0:
            raise APIError("returned no result")
        result = {"total": response["data"]["total"], "result": reply}
        return result
    
    def make_request_without_params(self, method_url: str) -> Optional[Any]:
        params = {}
        params["api_key"] = self.api_key
        response = requests.get(self.endpoint_uri + method_url, params=params).json()
        if response.get("error"):
            raise APIError(response["error"])
        return response
