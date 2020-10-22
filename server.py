import database as db
import settings

app = settings.app


@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run(debug=True, use_reloader=True)
