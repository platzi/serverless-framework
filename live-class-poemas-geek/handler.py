import json
import urllib.request
import os

def generarPoema(event, context):
    body = json.loads(event['body'])

    romantico = body['romantico']
    num_palabras = body['numero_max_palabras']
    lenguaje = body['lenguaje_de_programacion']

    prompt = f"Generar un poema {'romántico' if romantico else 'no romántico'} sobre {lenguaje} con un máximo de {num_palabras} palabras.\n\n"
    engine = "text-davinci-003"

    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": num_palabras,
    }


    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OPENAIKEY']}",
        "OpenAI-Organization": os.environ['OPENAIORG']
    }

    req = urllib.request.Request(
        url="https://api.openai.com/v1/completions",
        data=json.dumps(data).encode(),
        headers=headers,
        method="POST"
    )

    with urllib.request.urlopen(req) as res:
        res_data = json.loads(res.read().decode())

    poem = res_data["choices"][0]["text"]

    response = {
        "statusCode": 200,
        "body": json.dumps({"poema": poem})
    }

    return response
