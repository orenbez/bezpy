# TRY THIS: https://medium.com/better-programming/the-beginners-guide-to-pydantic-ba33b26cde89
# TRY THIS: https://www.educative.io/blog/python-fastapi-tutorial
# TRY THIS: https://www.infoworld.com/article/3629409/get-started-with-fastapi.html
# TRY THIS: https://www.makeuseof.com/build-api-python-popular-frameworks/



# FastApi uses Starlette (light-weight Asynchronous Web Framework)
#         uses Pydantic for typehints at runtime, user-friendly error messages
#         uses Uvicorn is an Async. server ASGI


# Note:
# Syntax for fastapi is similar to flask
# Requires Python 3.6+
# pip install fastapi  # This will install requirements starlette & pydantic
# pip install uvicorn  # This installs venv\Scripts\uvicorn.exe

# =======================================================================
# To Start Server run: uvicorn bezpy_60_fastapi:app --reload
# =======================================================================


# Documentation: https://fastapi.tiangolo.com
# Source Code: https://github.com/tiangolo/fastapi

# https://tiangolo.medium.com/introducing-fastapi-fdc1206d453f
# https://towardsdatascience.com/fastapi-has-ruined-flask-forever-for-me-73916127da
# Tutorial: https://youtu.be/0RS9W8MtZe4


# Advantages: Auto-generates API documentation, FastAPI makes it easy to build a GraphQL API with a Python library
#             called graphene-python. It is based and also compatible with the OpenAPI.
#             FastAPI integrates well with OAuth 2.0 and external providers.
# Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.
#                  Beats Flask & Django in performance
#                  FastAPI supports asynchronous code out of the box using the async/await Python keywords (unlike flask)
# Note: keywords async / await are new to version 3.4

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}  # Returns a python dictionary which gets converted to JSON response


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/async_item/{item_id}")
async def read_item(item_id: int, q: str = None):   # added the async keyword
    return {"async_item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


#  http://127.0.0.1:8000/ -> {"Hello":"World"}
#  http://127.0.0.1:8000/items/6 -> {"item_id":6,"q":null}
#  http://127.0.0.1:8000/items/5?q=somequery -> {"item_id":5,"q":"somequery"}
#  http://127.0.0.1:8000/items/hello?q=somequery -> {"detail":[{"loc":["path","item_id"],"msg":"value is not a valid integer","type":"type_error.integer"}]}
#  http://127.0.0.1:8000/async_item/9?q=somequery -> {"async_item_id":9,"q":"somequery"}
#  http://127.0.0.1:8000/docs ->  AUTOMATIC INTERACTIVE DOCUMENTATION ON THE API
