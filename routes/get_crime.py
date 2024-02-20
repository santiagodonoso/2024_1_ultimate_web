from bottle import get

##############################
@get("/crimes/<id>")
def _(id):
    return """
    <template mix-target="#info" mix-top>
        <div class="crime_info">
            <div>Male shot dog</div>
            <div>Urgent</div>
        </div>
    </template>
    """










