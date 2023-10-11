from apiHandler import APIHandler
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def webhook():
    handler = APIHandler()
    # Obtiene los datos JSON de la solicitud POST
    data = request.get_json()
    message= data["text"]

    aiResponse = handler.ai_request(message)
    return jsonify(aiResponse)

    # Realiza alguna lógica con los datos
    # En este ejemplo, simplemente devolvemos los datos recibidos

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
