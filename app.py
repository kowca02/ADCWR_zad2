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

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        result = 1 if (num1 + num2) > 5.8 else 0
        return jsonify({
            "prediction": result,
            "features": {
                "num1": num1,
                "num2": num2
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run()
