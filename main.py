import app as main

app = None

def start_app():
    global app
    app = main.App(reset_callback=reset_app)


def reset_app():

    start_app()


start_app()

