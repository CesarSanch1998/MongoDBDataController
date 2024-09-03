from fastapi import APIRouter
from fastapi import HTTPException
import os
from dotenv import load_dotenv
from db.connection import get_mongo_client
from schema.movie import insert_movies

load_dotenv()
get_data = APIRouter()


# ----------------------------------------------------------------------
# Clase obtener todos los datos de las peliculas almacenados
# ----------------------------------------------------------------------
@get_data.get("/data/{db}/{collection}/all")
def get_all_data(db:str, collection:str, api_key: str = None):
    # Api key smartolt ----------------------
    if api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    _book = []
    client = get_mongo_client()
    result = client["oztvtest"]["movies"].find()
    # print results
    for i in result:
        _book.append(i)
    client.close()
    return HTTPException(status_code=202, detail=_book)


# ----------------------------------------------------------------------
# Clase obtener 1 los dato de las peliculas almacenadas
# ----------------------------------------------------------------------
@get_data.get("/movie/data/{id_movie}")
async def get_one_movie_data(id_movie: int, api_key: str = None):
    # Api key smartolt ----------------------
    if api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    _book = []
    client = get_mongo_client()
    result = client["oztvtest"]["movies"].find({"id_moviedb": f"{id_movie}"})
    # print results
    for i in result:
        _book.append(i)
    client.close()
    print(f"aceptado cod: {id_movie}")
    # response = modify_plan_client(data.data)
    return HTTPException(status_code=202, detail=_book)


# ----------------------------------------------------------------------
# Clase obtener peliculas segun categoria
# ----------------------------------------------------------------------
@ops_movie_data.get("/movie/data/category/{category}")
async def get_all_movie_by_category(category: str, api_key: str = None):
    # Api key smartolt ----------------------
    if api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    response = f"aceptado cod: {category}"
    # response = modify_plan_client(data.data)
    return HTTPException(status_code=202, detail=response)


# ----------------------------------------------------------------------
# Clase obtener peliculas segun categoria
# ----------------------------------------------------------------------
@ops_movie_data.post("/movie/data")
async def insert_movie_data(data: insert_movies,api_key: str = None):
    # Api key smartolt ----------------------
    if api_key.strip() != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    # response = f"Insert Ok"
    data_to_insert = {
        "id_moviedb": data.id_movied,
        "title": data.title,
        "release_date": data.release_date,
        "genres": data.genres,
        "actores": data.actors,
        "sinopsis": data.description,
        "duracion": data.duration,
        "calificacion": data.calificacion,
        "trailer": data.trailer,
        "poster_path": data.poster_path,
        "backdrop_path": data.backdrop_path,
        "video_path": data.video_path,
    }
    client = get_mongo_client()
    
    insert = client["oztvtest"]["movies"].insert_one(data_to_insert)
    return_id = client["oztvtest"]["movies"].find_one(
        {"id_moviedb": data.id_movied}
    )
    response = {f"Correct insert in db by _id : {return_id["_id"]}"}
    client.close()
    # response = modify_plan_client(data.data)
    return HTTPException(status_code=202, detail=response)
