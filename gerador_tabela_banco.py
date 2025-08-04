import random
import psycopg2
from faker import Faker
from datetime import datetime, timedelta

# Inicializa o gerador de dados falsos
fake = Faker()
Faker.seed(42)
random.seed(42)

# Gerar 100 clientes únicos
clientes = [fake.name() for _ in range(100)]

# Define o intervalo de datas para as compras
start_date = datetime(2017, 1, 1)
end_date = datetime(2025, 2, 17)

# Define os preços históricos aproximados do BTC por ano (em BRL)
btc_prices = {
    2017: (6000, 130000),
    2018: (24000, 110000),
    2019: (20000, 90000),
    2020: (50000, 120000),
    2021: (60000, 700000),
    2022: (120000, 440000),
    2023: (180000, 500000),
    2024: (600000, 700000),  # Faixa fixada para testes
    2025: (500000, 600000)   # Faixa fixada para testes
}

# Função para gerar uma data aleatória entre duas datas
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Conexão com o banco de dados PostgreSQL hospedado na Render
conn = psycopg2.connect(
    dbname="transacoes_btc_hb1p",
    user="transacoes_btc_user",
    password="91aWWKQHFBmqWm1IqP0RCf6XH5C5Qko7",
    host="dpg-d28bttur433s73e1jcfg-a.ohio-postgres.render.com",
    port="5432"
)
cur = conn.cursor()

# Cria (ou recria) a tabela no banco
cur.execute('''
    DROP TABLE IF EXISTS transacoes_clientes;
    CREATE TABLE IF NOT EXISTS transacoes_clientes (
        id SERIAL PRIMARY KEY,
        cliente VARCHAR(100),
        data_compra TIMESTAMP,
        preco_btc DECIMAL(10,2),
        quantidade_btc DECIMAL(10,5)
    )
''')
conn.commit()

# Gera de 3 a 10 transações por cliente
for cliente in clientes:
    num_transacoes = random.randint(3, 10)
    for _ in range(num_transacoes):
        # Gera uma data de compra aleatória
        data_compra = random_date(start_date, end_date)
        ano = data_compra.year

        # Define a faixa de preço do BTC com base no ano
        preco_min, preco_max = btc_prices.get(ano, (150000, 350000))

        # Gera o preço e a quantidade de BTC para essa compra
        preco_btc = round(random.uniform(preco_min, preco_max), 2)
        quantidade_btc = round(random.uniform(0.001, 1.5), 5)

        # Insere a transação no banco
        cur.execute(
            "INSERT INTO transacoes_clientes "
            "(cliente, data_compra, preco_btc, quantidade_btc) "
            "VALUES (%s, %s, %s, %s)",
            (cliente, data_compra, preco_btc, quantidade_btc)
        )


# Finaliza a transação e fecha a conexão
conn.commit()
cur.close()
conn.close()

print("Transações inseridas no banco de dados com sucesso!")
