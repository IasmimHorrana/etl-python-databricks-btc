import pandas as pd
import psycopg2

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="transacoes_btc_hb1p",
    user="transacoes_btc_user",
    password="91aWWKQHFBmqWm1IqP0RCf6XH5C5Qko7",
    host="dpg-d28bttur433s73e1jcfg-a.ohio-postgres.render.com",
    port="5432"
)

# Consulta SQL
query = """
    SELECT cliente, data_compra, preco_btc, quantidade_btc 
    FROM transacoes_clientes
    ORDER BY data_compra DESC
"""

# Usando Pandas para ler diretamente do banco de dados
df_transacoes = pd.read_sql(query, conn)

# Fechar conexão com o banco de dados
conn.close()

display(df_transacoes)