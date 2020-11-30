from flask import Flask,jsonify

print(__name__)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/about')
def about():
    return "This some about"

@app.route('/data')
def data():
        return jsonify({"a": 1})
if __name__== "__main__":
    app.run(debug=True)