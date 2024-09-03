from typing import Optional, List
from pydantic import BaseModel,Field
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator



class insert_movies(BaseModel):
    id_movied: int
    title: str
    release_date: str
    genres: List[str]
    actors: List[str]
    description: str
    duration: int
    calificacion: float
    trailer: str
    poster_path: str
    backdrop_path: str
    video_path: str