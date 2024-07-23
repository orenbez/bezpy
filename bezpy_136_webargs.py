# Requires `pip install webargs`
# for parsing and validating HTTP request objects, with built-in support for popular web frameworks,
# including Flask, Django, Bottle, Tornado, Pyramid, Falcon, and aiohttp

from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

app = Flask(__name__)

@app.route("/")
@use_args({'name': fields.Str(required=True)}, location='query')
def index(args):
    return "Hello " + args["name"]

if __name__ == '__main__':
    app.run()

# e.g. enter http://localhost:5000/?name=dave
# Hello Dave