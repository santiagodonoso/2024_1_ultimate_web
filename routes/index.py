from bottle import get, template

@get("/")
def _():
    return template("index")













