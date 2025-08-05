# Criando a função para verificar lucro ou prejuízo
def verificar_lucro(preco_compra):
    if preco_compra < preco_atual_btc_real:
        return "Lucro"
    else:
        return "Prejuízo"

# Aplicando a função para categorizar cada transação
df_transacoes["status_financeiro"] = df_transacoes["preco_btc"].apply(verificar_lucro)

# Exibindo o DataFrame atualizado
display(df_transacoes)