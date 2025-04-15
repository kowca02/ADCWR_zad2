from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def moja_strona():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')
def hello():
    name = request.args.get("name", default="")
    if name:
        return f"Hello {name}!"
    return "Hello!"

if __name__ == '__main__':
    app.run()
