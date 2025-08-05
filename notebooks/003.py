# Criando coluna: mes_compra
df_transacoes["mes_compra"] = df_transacoes["data_compra"].dt.to_period("M").astype(str)

# Agrupando por mês e somando o total de compras
df_agrupado = df_transacoes.groupby("mes_compra")["total_de_compras"].sum().reset_index()
display(df_agrupado)

# Responde: "Quanto foi gasto no total em BTC em cada mês?"