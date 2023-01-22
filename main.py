from fastapi import FastAPI, Body, HTTPException, Request, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "My FastAPI app"
app.version = "0.0.1"


class Movie(BaseModel):
    # id: int | None = None
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula vacia",
                "year": 2022,
                "rating": 9.8,
                "category": "action",
            }
        }


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Fiction",
    },
    {
        "id": 2,
        "title": "Avengers",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 3,
        "title": "Batman",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 4,
        "title": "Super Man",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Comic",
    },
    {
        "id": 5,
        "title": "Tictanic",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Drama",
    },
]


@app.get("/")
def message():
    return HTMLResponse("<h1>Hello World</h1>")


@app.get("/movies", tags=["movies"])
def get_movies():
    return JSONResponse(content=movies)


@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int = Path(ge=1, le=2000)):
    movie = list(filter(lambda x: x["id"] == id, movies))
    # for item in movies:
    #     if item["id"] == id:
    #         return item
    # return 'no existe'
    # raise HTTPException(status_code=404, detail="Movie not found")
    # return movie if len(movie) > 0 else "No existe"
    return "No se encontró la película" if not movie else JSONResponse(content=movie[0])
    # return movie[0] or "No hay nada que ver"


@app.get("/movies/", tags=["movies"])
# def get_movies_by_category(category: str, year: int):
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    # return [ item for item in movies if item['category'] == category ]
    movie = list(filter(lambda x: x["category"].lower() == category.lower(), movies))
    return JSONResponse(content=movie)


@app.post("/movies", tags=["movies"])
def create_movie(movie: Movie):
    movies.append(movie)
    return JSONResponse(content={"message": "Se creo la pelicula"})
    # De esta forma no se valida los datos -------->
    # from fastapi import Request
    # movie = await request.json()
    # movies.append(movie)
    # return movie
    # Error TypeError: Body() missing 1 required positional argument: 'default' ------>
    # def create_movie(id: int = Body(default=1),
    #     title: str = Body(default="text"),
    #     year:int = Body(default=0),
    #     rating: float = Body(default=0),
    #     category: str = Body(default="text")):


@app.put("/movies/{id}", tags=["movies"])
def update_movie(id: int, movie: Movie):
    # for item in movies: ----------> Dict
    #     if item["id"] == id:
    #         item["title"] = movie.title
    #         item["overview"] = movie.overview
    #         item["year"] = movie.year
    #         item["rating"] = movie.rating
    #         item["category"] = movie.category
    #         return movies
    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.overview = movie.overview
            item.year = movie.year
            item.rating = movie.rating
            item.category = movie.category
            return JSONResponse(content={"message": "Se modifico la pelicula"})


@app.delete("/movies/{id}", tags=["movies"])
def delete_movie(id: int):
    # movies = list(filter(lambda x: x['id'] != id, movies))
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={"message": "Se elimino la pelicula"})
