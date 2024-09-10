from dataclasses import dataclass, field
from enum import Enum

from api_automation.api_utils.rest_api import RestApi, RestAction
from api_automation.configs.config_template import BASE_URL


@dataclass()
class StarWarsRestApi(RestApi):
    headers: dict = field(
        init=False,
        default_factory=lambda: {
            "Content-Type": "application/json",
            "Accept-Language": "zh-TW",
        },
    )


@dataclass()
class StarWarsRestAction(RestAction):
    host: str = field(default=BASE_URL)


class StarWarsFilmsErrResponseMessage(Enum):
    NOT_FOUND = "Not found"
    POST_NOT_ALLOW = "Method 'POST' not allowed."
