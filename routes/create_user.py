from bottle import post, request

@post("/users")
def _():
    user_name = request.forms.get("user_name")
    return f"""
    <template
        mix-target="#welcome"
    >
        <p>Hi {user_name}</p>
    </template>

    <template mix-target="#btn_create" mix-position="replace">

    </template>
    """