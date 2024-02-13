from bottle import delete

@delete("/items/<id>")
def _(id):
    # Validate
    # connect to the db
    # DELETE FROM items where item_id = ?
    return f"""
    <template
        mix-target="[id='{id}']"
        mix-position = "replace"
    >
    </template>

    <template
        mix-target="#message"
    >
       <div mix-live-for = "3000">Item {id} deleted</div> 
    </template>

    """