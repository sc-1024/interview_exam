from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional


# ============================== Films ==============================
class GetFilmDetailResponse(BaseModel):
    title: Optional[str] = (
        Field(default=None, description="The title of this film"))
    episode_id: Optional[int] = (
        Field(default=None, description="The episode number of this file"))
    opening_crawl: Optional[str] = (
        Field(default=None, description="The opening paragraphs at the beginning of this film"))
    director: Optional[str] = (
        Field(default=None, description="The name of the director of this film"))
    producer: Optional[str] = (
        Field(default=None, description="The name(s) of the producer(s) of this film. Comma separated."))
    release_date: Optional[str] = (
        Field(default=None, description="The ISO 8601 date format of film release at original creator country"))
    species: Optional[List[HttpUrl]] = (
        Field(default=None, description="An array of species resource URLs that are in this film"))
    starships: Optional[List[HttpUrl]] = (
        Field(default=None, description="An array of starship resource URLs that are in this film"))
    vehicles: Optional[List[HttpUrl]] = (
        Field(default=None, description="An array of vehicle resource URLs that are in this film"))
    characters: Optional[List[HttpUrl]] = (
        Field(default=None, description="An array of people resource URLs that are in this film"))
    planets: Optional[List[HttpUrl]] = (
        Field(default=None, description="An array of planet resource URLs that are in this film"))
    url: Optional[HttpUrl] = (
        Field(default=None, description="The hypermedia URL of this resource"))
    created: Optional[str] = (
        Field(default=None, description="The ISO 8601 date format of the time that this resource was created"))
    edited: Optional[str] = (
        Field(default=None, description="The ISO 8601 date format of the time that this resource was edited"))


class GetFilmDetailErrResponse(BaseModel):
    detail: str = Field(description="The error message")


class GetFilmListResponse(BaseModel):
    count: int = Field(description="The count of films")
    next: Optional[HttpUrl] = Field(description="The URL for the next page")
    previous: Optional[HttpUrl] = Field(description="The URL for the previous page")
    results: List[GetFilmDetailResponse] = Field(description="The list of films")


class OptionsFilmsResponse(BaseModel):
    name: str = Field(description="The name of this resource")
    description: str = Field(description="The description of this resource")
    renders: List[str] = Field(description="The list of content types that this resource can return")
    parses: List[str] = Field(description="The list of content types that this resource can consume")


class PostFilmsResponse(BaseModel):
    detail: str = Field(description="The name of this resource")


class FileListRequestParams(BaseModel):
    search: Optional[str] = Field(default=None, description="A search term to be applied to the films")
