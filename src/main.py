from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from config import DEBUG_STATUS, HOST, PORT


# Initilize Flask App
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

from views import *

if __name__ == "__main__":
    app.run(debug=DEBUG_STATUS, host=HOST, port=PORT)
