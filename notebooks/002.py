# Criando coluna: total_de_compras
# Representa o valor total em reais que o cliente gastou em uma única transação de compra de BTC.

df_transacoes["total_de_compras"] = (df_transacoes["preco_btc"] * df_transacoes["quantidade_btc"]).round(2)
display(df_transacoes)