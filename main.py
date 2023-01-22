from fastapi import FastAPI
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
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Vengadores",
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
]


@app.get("/")
def message():
    return HTMLResponse("<h1>Hello World</h1>")


@app.get("/movies", tags=["movies"])
def get_movies():
    return movies


@app.get("/movies/{id}")
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
