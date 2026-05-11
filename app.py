from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import markdown

app = Flask(__name__)
client = OpenAI(
    api_key=""
)

@app.route('/')
def index():
    # references the HTML file
	return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")

    response = client.responses.create(
        #custom GPT that is already prompt engineered
        prompt={
            "id": "pmpt_69ea771f557081978a3655abdcc4f9dd0c41a47a53eecaf4",
            "version": "3"
        },
        input=user_input
    )

    # converts to markdown
    formatted_response = markdown.markdown(response.output_text)

    return jsonify({
        "response": formatted_response
    })

if __name__ == "__main__":
    app.run(debug=True)

