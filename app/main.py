from fastapi import FastAPI
from .routers import example, example_celery

app = FastAPI()
app.include_router(example.router)
app.include_router(example_celery.router)


@app.get('/')
async def root():
    return {'message': 'Hello, world!'}
