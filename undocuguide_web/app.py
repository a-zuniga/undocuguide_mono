from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scholarships')
def scholarships():
    # Send a GET request to your API to retrieve the scholarship data
    r = requests.get('http://127.0.0.1:5000/scholarships')
    scholarships = r.json()
    return render_template('scholarships.html', scholarships=scholarships)



if __name__ == '__main__':
    app.run(port=8080, debug=True)
