from bottle import get

@get("/item")
def _():
    return """
    <template
    mix-target="body"
    mix-position="afterbegin"
    >
        <div mix-live-for="5000">
            Santiago
        </div>
    </template>
    """







