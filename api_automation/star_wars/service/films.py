from api_automation.api_utils.rest_api import HttpMethods
from api_automation.star_wars.rest_base import StarWarsRestApi, StarWarsRestAction
from api_automation.star_wars.models.films import (
    GetFilmListResponse,
    GetFilmDetailResponse,
    OptionsFilmsResponse,
    PostFilmsResponse,
    GetFilmDetailErrResponse,
    FileListRequestParams
)


class GetFilmDetailAPI(StarWarsRestApi):
    path: str = "/api/films/{film_id}"
    method: HttpMethods = HttpMethods.GET
    response_type = GetFilmDetailResponse

    def __post_init__(self):
        self.path = self.path.format(film_id=self._film_id)

    def set_film_id(self, film_id: str):
        self._film_id = film_id
        self.__post_init__()


class OptionsFilmDetailAPI(StarWarsRestApi):
    path: str = "/api/films/{film_id}"
    method: HttpMethods = HttpMethods.OPTIONS
    response_type = OptionsFilmsResponse

    def __post_init__(self):
        self.path = self.path.format(film_id=self._film_id)

    def set_film_id(self, film_id: str):
        self._film_id = film_id
        self.__post_init__()


class PostFilmDetailAPI(StarWarsRestApi):
    path: str = "/api/films/{film_id}"
    method: HttpMethods = HttpMethods.POST
    response_type = PostFilmsResponse

    def __post_init__(self):
        self.path = self.path.format(film_id=self._film_id)

    def set_film_id(self, film_id: str):
        self._film_id = film_id
        self.__post_init__()


class GetFilmListAPI(StarWarsRestApi):
    path: str = "/api/films"
    method: HttpMethods = HttpMethods.GET
    response_type = GetFilmListResponse


class OptionsFilmListAPI(StarWarsRestApi):
    path: str = "/api/films"
    method: HttpMethods = HttpMethods.OPTIONS
    response_type = OptionsFilmsResponse


class PostFilmListAPI(StarWarsRestApi):
    path: str = "/api/films"
    method: HttpMethods = HttpMethods.POST
    response_type = PostFilmsResponse


class FilmService(StarWarsRestAction):

    def request_get_file_list_response_headers(self):
        api = GetFilmListAPI(host=self.host)
        resp = api.request()
        return resp.headers

    def request_get_file_detail_response_headers(self, film_id: str):
        api = GetFilmDetailAPI(host=self.host)
        api.set_film_id(film_id)
        resp = api.request()
        return resp.headers

    def request_get_film_list(self, **query) -> GetFilmListResponse:
        api = GetFilmListAPI(host=self.host)
        params = FileListRequestParams(**query).model_dump(by_alias=True)
        resp = api.request(params=params)
        return GetFilmListResponse(**resp.json())

    def request_get_film_detail(self, film_id: str) -> GetFilmDetailErrResponse | GetFilmDetailResponse:
        api = GetFilmDetailAPI(host=self.host)
        api.set_film_id(film_id)
        resp = api.request()
        if resp.status_code != 200:
            return GetFilmDetailErrResponse(**resp.json())
        else:
            return GetFilmDetailResponse(**resp.json())

    def request_options_film_list(self) -> OptionsFilmsResponse:
        api = OptionsFilmListAPI(host=self.host)
        resp = api.request()
        return OptionsFilmsResponse(**resp.json())

    def request_options_film_detail(self, film_id: str) -> OptionsFilmsResponse:
        api = OptionsFilmDetailAPI(host=self.host)
        api.set_film_id(film_id)
        resp = api.request()
        return OptionsFilmsResponse(**resp.json())

    def request_post_film_list(self) -> PostFilmsResponse:
        api = PostFilmListAPI(host=self.host)
        resp = api.request()
        return PostFilmsResponse(**resp.json())

    def request_post_film_detail(self, film_id: str) -> PostFilmsResponse:
        api = PostFilmDetailAPI(host=self.host)
        api.set_film_id(film_id)
        resp = api.request()
        return PostFilmsResponse(**resp.json())
