from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data["question"]

    return jsonify({
        "answer": f"[MOCK AI] You asked: {question}. This system analyzes CI/CD pipelines and suggests improvements."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)