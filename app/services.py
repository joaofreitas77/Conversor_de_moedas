def converter_moeda(origem, destino, valor):
    import requests

    url = f"https://api.frankfurter.dev/v1/latest?base={origem}&symbols={destino}"
    
    response = requests.get(url)
    data = response.json()

    taxa = data['rates'][destino]

    return valor * taxa