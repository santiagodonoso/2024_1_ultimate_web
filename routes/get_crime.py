from bottle import get, template

##############################
@get("/crimes/<id>")
def _(id):
    return template("_crime")










