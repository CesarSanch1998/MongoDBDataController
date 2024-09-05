from fastapi import APIRouter
from fastapi import HTTPException
import os
from dotenv import load_dotenv
from db.connection import get_mongo_client
from schema.movie import insert_movies


load_dotenv()
insert_data = APIRouter()


# # ----------------------------------------------------------------------
# # Clase obtener peliculas segun categoria
# # ----------------------------------------------------------------------
@insert_data.post("/api/insert/movie")
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
    
    insert = client[os.environ["DB_NAME"]][os.environ["DB_COLLECTION"]].insert_one(data_to_insert)
    return_id = client[os.environ["DB_NAME"]][os.environ["DB_COLLECTION"]].find_one(
        {"id_moviedb": data.id_movied}
    )
    response = {f"Correct insert in db by _id : {return_id['_id']}"}
    client.close()
    # response = modify_plan_client(data.data)
    return HTTPException(status_code=202, detail=response)
