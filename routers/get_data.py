from fastapi import APIRouter
from fastapi import HTTPException
import os
from dotenv import load_dotenv
from db.connection import get_mongo_client

load_dotenv()
get_data = APIRouter()


# https://tudominio.com/api/search?db={db_name}&collection={collection_name}&apikey={api_key}&filter={filter_value}
# ----------------------------------------------------------------------
# Clase obtener todos los datos de las peliculas almacenados
# ----------------------------------------------------------------------
@get_data.get("/api/search/all")
def get_all_data(api_key: str = None):
    # Api key smartolt ----------------------
    if api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    _book = []
    client = get_mongo_client()
    result = client["oztvtest"]["movies"].find({}, {"_id": 0}) # por errores trae todos los campos excepto el _id
    for i in result:
        _book.append(i)
    client.close()
    return HTTPException(status_code=202, detail=_book)


# ----------------------------------------------------------------------
# Clase para obtener peliculas por categoria
# ----------------------------------------------------------------------
@get_data.get("/api/search/category/{category}")
def get_all_data(category:str, api_key: str = None):
    # Api key smartolt ----------------------
    if api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    _book = []
    client = get_mongo_client()
    result = client["oztvtest"]["movies"].find({"genres": f"{category}"}, {"_id": 0}) # por errores trae todos los campos excepto el _id
    # print results
    for i in result:
        _book.append(i)
    client.close()
    return HTTPException(status_code=202, detail=_book)

# ----------------------------------------------------------------------
# Clase para obtener detalles de peliculas por id
# ----------------------------------------------------------------------
@get_data.get("/api/search/detail/{id_movie}")
def get_all_data(id_movie:str, api_key: str = None):
    # Api key smartolt ----------------------
    if api_key != os.environ["API_KEY"]:
        return HTTPException(status_code=401, detail="Invalid API key")
    _book = []
    client = get_mongo_client()
    result = client["oztvtest"]["movies"].find({"id_moviedb": f"{id_movie}"}, {"_id": 0}) # por errores trae todos los campos excepto el _id
    # print results
    for i in result:
        _book.append(i)
    client.close()
    return HTTPException(status_code=202, detail=_book)


# # ----------------------------------------------------------------------
# # Clase obtener 1 los dato de las peliculas almacenadas
# # ----------------------------------------------------------------------
# @get_data.get("/data/{db}/{collection}/title")
# async def get_one_movie_data(db:str, collection:str, tittle: str, api_key: str = None):
#     # Api key smartolt ----------------------
#     if api_key != os.environ["API_KEY"]:
#         return HTTPException(status_code=401, detail="Invalid API key")
#     _book = []
#     client = get_mongo_client()
#     result = client["oztvtest"]["movies"].find({"id_moviedb": f"{id_movie}"})
#     # print results
#     for i in result:
#         _book.append(i)
#     client.close()
#     print(f"aceptado cod: {id_movie}")
#     # response = modify_plan_client(data.data)
#     return HTTPException(status_code=202, detail=_book)


# # ----------------------------------------------------------------------
# # Clase obtener peliculas segun categoria
# # ----------------------------------------------------------------------
# @ops_movie_data.get("/movie/data/category/{category}")
# async def get_all_movie_by_category(category: str, api_key: str = None):
#     # Api key smartolt ----------------------
#     if api_key != os.environ["API_KEY"]:
#         return HTTPException(status_code=401, detail="Invalid API key")
#     response = f"aceptado cod: {category}"
#     # response = modify_plan_client(data.data)
#     return HTTPException(status_code=202, detail=response)


