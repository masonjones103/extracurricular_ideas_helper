from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(
    api_key=""
)

@app.route('/')
def index():
	return render_template('index.html')
def chat():
    user_message = request.json.get("message")

    response = client.responses.create(
        prompt={
            "id": "pmpt_69ea771f557081978a3655abdcc4f9dd0c41a47a53eecaf4",
            "version": "3"
        }
    )

    return jsonify({
        "reply": response.output_text
    })

if __name__ == "__main__":
    app.run(debug=True)

