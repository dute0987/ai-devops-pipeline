from flask import Flask, request, jsonify

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return "Chatbot is running. Use POST /ask to ask questions."

# Chat endpoint
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data["question"]

    return jsonify({
        "answer": f"[MOCK AI] You asked: {question}. This system analyzes CI/CD pipelines and suggests improvements."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)