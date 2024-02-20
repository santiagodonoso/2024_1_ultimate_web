from bottle import get, default_app, static_file

##############################
@get("/app.css")
def _():
    return static_file("app.css", ".")


##############################
@get("/map.png")
def _():
    return static_file("map.png", ".")



##############################
@get("/mixhtml.js")
def _():
    return static_file("mixhtml.js", ".")


##############################
import routes.index
import routes.get_item
import routes.delete_item
import routes.create_user

import routes.get_crime


app = default_app

# python -m bottle --server paste --bind 127.0.0.1:80 --debug --reload app