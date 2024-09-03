from typing import Optional, List
from pydantic import BaseModel,Field
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

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

# class list_movies(BaseModel):
#     movies: List[movies]

# {
#     "_id": ObjectId("5f977fa4734d1d30f47d2399"),
#     "id_moviedb": 533535,
#     "title": "Deadpool & Wolverine",
#     "release_date": "2024-07-24",
#     "genres": ["Drama", "Crimen"],
#     "actores": ["Marlon Brando", "Al Pacino"],
#     "sinopsis": "Un poderoso jefe de la mafia italiana en Nueva York transfiere el control de su imperio criminal a su reluctante hijo.",
#     "duracion": 175,
#     "calificacion": 9.2,
#     "poster": "https://image.tmdb.org/t/p/w500/kBwSAAQuWSMa3pB7ZpQ6l94z54B.jpg", 
#     "trailer": "https://www.youtube.com/watch?v=sY1S349qZFe",
#     "poster_path":"/30c5jO7YEXuF8KiWXLg9m28GWDA.jpg",
#     "backdrop_path": "/hBQOWY8qWXJVFAc8yLTh1teIu43.jpg",
#     "video_path": "/hBQOWY8qWXJVFAc8yLTh1teIu43.jpg"
# },