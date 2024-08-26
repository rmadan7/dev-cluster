from flask import Flask, request

app = Flask(__name__)

@app.route("/")

@app.route("/sum", methods=["POST"])
def hello():
    reqJson = request.get_json()
    x = reqJson['x']
    y = reqJson['y']
    sum = x + y
    return {"result":sum}

if __name__ == '__main__':
    # publishes on localhost and and a private port
    app.run(host='0.0.0.0', port=50100, debug=True)