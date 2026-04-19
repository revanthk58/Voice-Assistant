from  flask import Flask, render_template, request, jsonify
from core.assistant import get_response


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({"response": "Invalid request"}), 400

    user_input = data["message"]

    response = get_response(user_input)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)