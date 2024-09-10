import requests
from dataclasses import dataclass, field
from enum import Enum
from pydantic import BaseModel
from typing import Optional
from urllib.parse import urljoin


from api_automation.common_utils.logger import LoggerManager

logger = LoggerManager.get_instance()


@dataclass()
class RestAction:
    host: str = field()


class HttpMethods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


@dataclass()
class RestApi:
    session = requests.Session()
    host: str = field(default="")
    path: str = field(init=False, default="")
    method: HttpMethods = field(init=False, default=HttpMethods.GET)
    headers: Optional[dict] = field(init=False, default=None)
    request_data_type: BaseModel = field(init=False, default=BaseModel)
    response_type: BaseModel = field(init=False, default=BaseModel)

    def request(
        self,
        *,
        method=None,
        params=None,
        data=None,
        headers=None,
        auth=None,
        **kwargs,
    ) -> requests.Response:
        path = self.path
        url = urljoin(self.host, path)
        method = method or self.method.value
        headers = headers or self.headers
        resp = self.session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            **kwargs,
        )
        if resp.request.body:
            logger.debug(resp.request.body)
        logger.info(f"Request url = {resp.url}, status code = {resp.status_code}")
        logger.debug(resp.json())
        return resp
