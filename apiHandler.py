import requests
from decouple import config
class APIHandler:
    def __init__(self) -> None:
        self.api_key = config("OPENAIKEY")
        self.url = config("VFAPI")
    def ai_request(self,message:str):
        print(message)
        
        reply = ""
        
        #print(user_id)
        body = {"action": {"type": "text", "payload": message}}
        
        # Start a conversation
        
        
        
        
        try:

            response = requests.post(url=self.url,
            json=body,
            headers={"Authorization": self.api_key},)

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
                            reply = self.message_payload = {
                            "fulfillment_response": {
                                "messages": [
                                {
                                    "text": {
                                        "text":[mensaje]
                                    }
                                }
                                ]
                            }
                        }

                            return reply
                        raise ValueError("Error conjunto vacío")
        except:
            reply = {
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
            return reply
