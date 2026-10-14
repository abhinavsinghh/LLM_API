from langchain.chat_models import init_chat_model
import flask
from flask import jsonify, Flask, request

app = Flask(__name__)

model = init_chat_model(
    model='llama3.2:latest',
    model_provider='ollama'
)

@app.route(rule='/chat', methods=['POST'])
def chat():
    data = request.get_json()
    print(data)
    response = model.invoke(data['messages'])
    return jsonify(
        {'message': {'role':'assistant',
                     'content': response.content}}
        )

if __name__ == '__main__':
    app.run(debug=True, port = 5002)