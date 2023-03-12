from flask import Flask

app = Flask(__name__)

from scholarships import scholarships
app.register_blueprint(scholarships)

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)