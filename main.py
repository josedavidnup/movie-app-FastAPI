from fastapi import FastAPI

app = FastAPI()
app.title = 'My FastAPI app'
app.version = '0.0.1'

@app.get('/')
def message():
    return 'Hello World'

@app.get('/contact')
def message():
    return 'Hello Contact'