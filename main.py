import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
def ai_request(message:str):
    print(message)
    
    reply = ""

    api_key = "VF.DM.64a759ba45738800080aaf32.CAfwpMtj32ur4tuW"

    
    #print(user_id)
    body = {"action": {"type": "text", "payload": message}}
    url = f"https://general-runtime.voiceflow.com/state/user/user_123/interact"
    # Start a conversation
    
    
    
    try:

        response = requests.post(url=url,
        json=body,
        headers={"Authorization": api_key},)

        print(response.text)
        for trace in response.json():
                if trace['type'] == 'speak' or trace['type'] == 'text':
                    mensaje = trace['payload']['message']
                    # Texto que deseas eliminar
                    text_to_remove = "I'm sorry for the confusion earlier. Here are the answers: - "
                    other_text = "I apologize for the mistake earlier. Here are the answers: - "
                    # Reemplazar el texto no deseado con una cadena vacía
                    mensaje = mensaje.replace(text_to_remove, "")
                    mensaje = mensaje.replace(other_text, "")
                    print(type(mensaje))
                    if mensaje!="":
                        reply = {
                                "fulfillmentMessages":[
                                {
                                    "text": 
                                    {
                                        "text": [
                                            mensaje                                         
                                        ]
                                    }
                                }
                                ]
                                }

                        return reply
                    raise ValueError("Error conjunto vacío")
    except:
        {
            "fulfillmentMessages":[
                {
                    "text": 
                    {
                        "text": [
                            "Lo sentimos, estamos mejorando la calidad de nuestro servicio de Chatbot. ¿Puedes volver a realizar la consulta?"                                         
                        ]
                    }
                }
                ]
        }

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', methods=['POST'])
def webhook():
    # Obtiene los datos JSON de la solicitud POST
    data = request.get_json()
    message= data["queryResult"]["queryText"]
    ai_request(message)

    # Realiza alguna lógica con los datos
    # En este ejemplo, simplemente devolvemos los datos recibidos

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
