from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, expose_headers=['Content-Range'])

from scholarships import scholarships
app.register_blueprint(scholarships)

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)