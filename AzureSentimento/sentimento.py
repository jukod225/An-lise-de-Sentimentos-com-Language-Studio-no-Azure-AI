import requests
import json

# Substitua com o seu endpoint e chave
endpoint = "https://<SEU-ENDPOINT>.cognitiveservices.azure.com/"
key = "<SUA-CHAVE-DA-API>"

# URL da API para análise de sentimentos
url = endpoint + "/language/:analyze-text?api-version=2023-04-01"

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/json"
}

# Texto que você quer analisar
document = {
    "kind": "SentimentAnalysis",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "language": "pt",
                "text": "Hoje o dia está maravilhoso e eu estou muito feliz!"
            }
        ]
    }
}

# Envia o texto para a API
response = requests.post(url, headers=headers, json=document)

# Imprime o resultado com indentação bonitinha
print(json.dumps(response.json(), indent=4, ensure_ascii=False))
