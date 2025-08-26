from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data' : {'name': 'Vza'}}

@app.get('/about')
def about():
    return {'data' : "about page"}

@app.get('/contact')
def contact():
    return {'data' : "my contact page"}

@app.get('/blog')
def blog():
    return {'data' : "my blog page"}