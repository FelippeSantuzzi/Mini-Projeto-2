from sqlalchemy import create_engine, MetaData, Table, Column, Integer
from sqlalchemy import String, Date, DateTime, text
from datetime import datetime
import csv
import time
import logging


engine = create_engine(
    "postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2"
)

metadata = MetaData()


usuarios = Table(
    'usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False, index=True),
    Column('cpf', String(14), nullable=False),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)


metadata.create_all(engine)


def LGPD(row):
    id, nome, cpf, email, telefone, data_nasc, created, updated = row

    partes_nome = nome.split()
    primeiro_nome = partes_nome[0]
    sobrenome = " ".join(partes_nome[1:]) if len(partes_nome) > 1 else ""
    nome_mask = primeiro_nome[0] + "*" * (len(primeiro_nome) - 1)
    nome_final = f"{nome_mask} {sobrenome}".strip()

    cpf_mask = cpf[:3] + ".***.***-**"

    user, dominio = email.split("@")
    email_mask = user[0] + "*" * (len(user) - 1) + "@" + dominio

    telefone_mask = telefone[-4:]

    return (
        id,
        nome_final,
        cpf_mask,
        email_mask,
        telefone_mask,
        data_nasc,
        created,
        updated
    )
# Atividade 4 (Decorador de tempo)
logging.basicConfig(
    filename="execucao.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()  

        resultado = func(*args, **kwargs)

        fim = time.time()  
        tempo = fim - inicio

        mensagem = f"{func.__name__} executado em {tempo:.4f} segundos"

        print(mensagem)        
        logging.info(mensagem) 

        return resultado
    return wrapper


# Atividade 2 com Medidor de Tempo
@medir_tempo
def atividade2():
    dados_por_ano = {}

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM usuarios;"))

        for row in result:
            row = LGPD(row)
            ano = row[5].year

            if ano not in dados_por_ano:
                dados_por_ano[ano] = []

            dados_por_ano[ano].append(row)

    for ano, registros in dados_por_ano.items():
        with open(f"{ano}.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id","nome","cpf","email","telefone","data_nasc","created","updated"])
            writer.writerows(registros)

        print(f"Arquivo {ano}.csv criado com {len(registros)} registros")


# Atividade 3 também com Medidor de Tempo
@medir_tempo
def atividade3():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT nome, cpf FROM usuarios;"))

    with open("todos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nome", "cpf"])

        for row in result:
            writer.writerow(row)

print("Arquivo todos.csv criado com sucesso")

atividade2()
atividade3()