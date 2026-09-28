import app as _app

app = None

def start_app():
    global app
    app = _app.App(reset_callback=reset_app)


def reset_app():

    start_app()

start_app()

