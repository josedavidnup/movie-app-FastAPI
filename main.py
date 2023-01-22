from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My FastAPI app"
app.version = "0.0.1"

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
    return movies


@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    movie = list(filter(lambda x: x["id"] == id, movies))
    # for item in movies:
    #     if item["id"] == id:
    #         return item
    # return 'no existe'
    # raise HTTPException(status_code=404, detail="Movie not found")
    # return movie if len(movie) > 0 else "No existe"
    return "No se encontró la película" if not movie else movie[0]
    # return movie[0] or "No hay nada que ver"


@app.get("/movies/", tags=["movies"])
# def get_movies_by_category(category: str, year: int):
def get_movies_by_category(category: str):
    # return [ item for item in movies if item['category'] == category ]
    movie = list(filter(lambda x: x["category"].lower() == category.lower(), movies))
    return movie


@app.post("/movies", tags=["movies"])
def create_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body(),
):
    movies.append(
        {
            "id": id,
            "title": title,
            "overview": overview,
            "year": year,
            "rating": rating,
            "category": category,
        }
    )
    return movies
    # De esta forma no se valida los datos -------->
    # from fastapi import Request
    # movie = await request.json()
    # movies.append(movie)
    # return movie
    # Error TypeError: Body() missing 1 required positional argument: 'default'
    # def create_movie(id: int = Body(default=1),
    #     title: str = Body(default="text"),
    #     year:int = Body(default=0),
    #     rating: float = Body(default=0),
    #     category: str = Body(default="text")):
