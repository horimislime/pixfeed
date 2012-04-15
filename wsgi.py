import sys
from pixfeed import app

app.debug=True
def application(environ,start_response):
    return app(environ,start_response)
