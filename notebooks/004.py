# Consumindo API do Bitcoin em tempo real, com preço já convertido para BRL (Real)

!pip install requests

import requests

def obter_preco_btc_em_reais():
    try:
        # Preço do Bitcoin em USD
        url_btc = "https://api.coinbase.com/v2/prices/spot?currency=USD"
        response_btc = requests.get(url_btc)
        preco_btc_usd = float(response_btc.json()['data']['amount'])

        # Cotação do dólar em BRL
        url_dolar = "https://economia.awesomeapi.com.br/last/USD-BRL"
        response_dolar = requests.get(url_dolar)
        cotacao_dolar = float(response_dolar.json()['USDBRL']['bid'])

        # Conversão para reais
        preco_btc_brl = preco_btc_usd * cotacao_dolar
        return preco_btc_brl

    except Exception as e:
        print(f"Erro ao obter cotação: {e}")
        return None

preco_atual_btc_real = obter_preco_btc_em_reais()
print(f"Preço atual do BTC em BRL: R$ {preco_atual_btc_real:,.2f}")
