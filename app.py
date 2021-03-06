from flask import Flask, g, jsonify
from flask_cors import CORS, cross_origin

from auth import auth
import config
import models
from resources.users import users_api


app = Flask(__name__)
app.register_blueprint(users_api, url_prefix='/api/v1')
CORS(app)


@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
