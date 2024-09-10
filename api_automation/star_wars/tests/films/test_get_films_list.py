import pytest
import requests

from api_automation.common_utils.logger import LoggerManager
from api_automation.star_wars.service.films import FilmService
from api_automation.star_wars.rest_base import StarWarsFilmsErrResponseMessage
from api_automation.star_wars.data.film.test_data import (
    film_list_required_fields,
    film_list,
    film_list_options_resp,
)

logger = LoggerManager.get_instance()


class TestFilmsList:

    @pytest.mark.list
    def test_get_film_list_verify_field_data_types(self):
        # pydantic will check the data types of the fields
        resp = FilmService().request_get_film_list()
        logger.info(f"resp: {resp}")
        assert resp is not None

    @pytest.mark.list
    def test_get_film_list_verify_film_fields_integrity(self):
        resp = FilmService().request_get_film_list()
        logger.info(f"resp: {resp}")
        resp_dict = resp.dict()
        for field in film_list_required_fields:
            assert field in resp_dict

    @pytest.mark.list
    def test_get_film_list_verify_film_lists(self):
        resp = FilmService().request_get_film_list()
        logger.info(f"resp: {resp}")
        resp_dict = resp.dict()
        for field, value in resp_dict.items():
            assert value == film_list[field]

    @pytest.mark.list
    def test_get_film_list_search_by_title(self):
        resp = FilmService().request_get_film_list(search="A New Hope")
        logger.info(f"resp: {resp}")
        assert resp.count == 1
        assert resp.results[0].title == "A New Hope"

    @pytest.mark.list
    def test_get_film_list_search_by_invalid_title(self):
        resp = FilmService().request_get_film_list(search="No Hope")
        logger.info(f"resp: {resp}")
        assert resp.count == 0
        assert resp.results == []

    @pytest.mark.list
    def test_get_film_list_pagination_check(self):
        resp = FilmService().request_get_film_list()
        logger.info(f"resp: {resp}")
        # 資料面上無 pagination 此 case 僅作記錄有此測試案例
        assert resp.next is None
        assert resp.previous is None

    @pytest.mark.list
    def test_get_film_list_verify_content_type(self):
        resp = FilmService().request_get_file_list_response_headers()
        logger.info(f"resp: {resp}")
        assert resp["Content-Type"] == "application/json"

    @pytest.mark.list
    def test_get_film_list_options_request(self):
        resp = FilmService().request_options_film_list()
        logger.info(f"resp: {resp}")
        resp_dict = resp.dict()
        for field, value in resp_dict.items():
            assert value == film_list_options_resp[field]

    @pytest.mark.list
    def test_get_film_other_method_to_request(self):
        resp = FilmService().request_post_film_list()
        logger.info(f"resp: {resp}")
        assert resp.detail == StarWarsFilmsErrResponseMessage.POST_NOT_ALLOW.value

    @pytest.mark.list
    def test_get_film_list_performance(self):
        num_of_request = 5
        response_times = []

        for _ in range(num_of_request):
            resp = requests.get(f"https://swapi.dev/api/films")
            logger.info(f"resp: {resp}")
            response_times.append(resp.elapsed.total_seconds())
            assert resp.elapsed.total_seconds() < 5

        avg_response_time = sum(response_times) / num_of_request
        assert avg_response_time < 10  # 這要再定義，可以用其他工具做會更好
