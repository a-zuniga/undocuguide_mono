from flask import Flask

app = Flask(__name__)

from scholarships import scholarships
app.register_blueprint(scholarships)

if __name__ == '__main__':
    app.run(debug=True)