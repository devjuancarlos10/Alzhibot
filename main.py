import openai

# Crear una instancia del cliente de OpenAI con la clave de API
api_key = "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"
client = openai(api_key=api_key)

while True:
    pregunta = input("Ingrese su pregunta: ")

    # Definir los mensajes para la solicitud de completado de conversación
    messages = [
        {"role": "system", "content": "eres un cuidador de personas con alzheimer "},
        {"role": "user", "content": pregunta}
    ]

    # Realizar la solicitud de completado de conversación
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100
    )

    # Obtener la respuesta generada por el modelo
    respuesta = completion.choices[0].message.content

    # Imprimir la respuesta generada
    print(respuesta)
    
    
    # response['choices'][0]['menssage']['content'])  
    
