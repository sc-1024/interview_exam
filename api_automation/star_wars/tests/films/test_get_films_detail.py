import pytest
import random
import re
import requests

from api_automation.common_utils.logger import LoggerManager
from api_automation.star_wars.service.films import FilmService
from api_automation.star_wars.rest_base import StarWarsFilmsErrResponseMessage
from api_automation.star_wars.data.film.test_data import (
    film_detail_required_fields,
    film_1_details,
    film_detail_options_resp,
)


logger = LoggerManager.get_instance()


class TestFilmDetail:

    @pytest.mark.detail
    def test_get_film_detail_verify_field_data_types(self):
        # pydantic will check the data types of the fields
        resp = FilmService().request_get_film_detail("1")
        logger.info(f"resp: {resp}")
        assert resp is not None

    @pytest.mark.detail
    def test_get_film_detail_verify_film_fields_integrity(self):
        resp = FilmService().request_get_film_detail("1")
        logger.info(f"resp: {resp}")
        resp_dict = resp.dict()
        for field in resp_dict:
            assert field in film_detail_required_fields

    @pytest.mark.detail
    def test_verify_film_details(self):
        resp = FilmService().request_get_film_detail("1")
        logger.info(f"resp: {resp}")
        resp_dict = resp.dict()
        for field, value in resp_dict.items():
            assert value == film_1_details[field]

    @pytest.mark.detail
    def test_get_film_detail_invalid_film_id_int(self):
        resp = FilmService().request_get_film_detail("9999")
        logger.info(f"resp: {resp}")
        assert resp.detail == StarWarsFilmsErrResponseMessage.NOT_FOUND.value

    @pytest.mark.detail
    def test_get_film_detail_invalid_film_id_string(self):
        resp = FilmService().request_get_film_detail("steven")
        logger.info(f"resp: {resp}")
        assert resp.detail == StarWarsFilmsErrResponseMessage.NOT_FOUND.value

    @pytest.mark.detail
    def test_get_film_detail_verify_date_format(self):
        resp = FilmService().request_get_film_detail("1")
        logger.info(f"resp: {resp}")
        release_date_regex = r"\d{4}-\d{2}-\d{2}"
        date_regex = "^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z$"
        assert re.match(release_date_regex, str(resp.release_date))
        assert re.match(date_regex, str(resp.created))
        assert re.match(date_regex, str(resp.edited))
        assert resp.created < resp.edited

    @pytest.mark.detail
    def test_get_film_detail_verify_associated_resources(self):
        resp = FilmService().request_get_film_detail("1")
        logger.info(f"resp: {resp}")
        resp_dict = resp.dict()

        associated_resources = ["species", "starships", "vehicles", "characters", "planets"]

        for resource in associated_resources:
            url = random.choice(resp_dict[resource])
            res = requests.get(url)
            assert res.status_code == 200

    @pytest.mark.detail
    def test_get_film_detail_verify_content_type(self):
        resp = FilmService().request_get_file_detail_response_headers("1")
        logger.info(f"resp: {resp}")
        assert resp["Content-Type"] == "application/json"

    @pytest.mark.detail
    def test_get_film_detail_options_request(self):
        resp = FilmService().request_options_film_detail("1")
        logger.info(f"resp: {resp}")
        resp_dict = resp.dict()
        for field, value in resp_dict.items():
            assert value == film_detail_options_resp[field]

    @pytest.mark.detail
    def test_get_film_detail_other_method_to_request(self):
        resp = FilmService().request_post_film_detail("1")
        logger.info(f"resp: {resp}")
        assert resp.detail == StarWarsFilmsErrResponseMessage.POST_NOT_ALLOW.value

    @pytest.mark.detail
    def test_get_film_detail_sql_injection(self):
        resp = FilmService().request_get_film_detail("'; DROP TABLE; --")
        logger.info(f"resp: {resp}")
        assert resp.detail == StarWarsFilmsErrResponseMessage.NOT_FOUND.value

    @pytest.mark.detail
    def test_get_film_detail_performance(self):

        response_times = []
        film_ids = [1, 2, 3, 4, 5, 6]

        for film in film_ids:
            resp = requests.get(f"https://swapi.dev/api/films/{str(film)}")
            logger.info(f"resp: {resp}")
            response_times.append(resp.elapsed.total_seconds())
            assert resp.elapsed.total_seconds() < 5

        avg_response_time = sum(response_times) / len(film_ids)
        assert avg_response_time < 10  # 這邊要再定義，可以用其他工具做會更好
