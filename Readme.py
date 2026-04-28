# Mini Projeto 2 - LGPD

# Descrição
Projeto em Python que acessa um banco PostgreSQL, aplica anonimização de dados e gera arquivos CSV.

---

# Tecnologias
* Python 3
* SQLAlchemy
* psycopg2

---

# Execução

1. Clonar repositório

git clone <url-do-repositorio>
cd Mini-Projeto-2


# 2. Criar ambiente virtual

python3 -m venv venv


# 3. Ativar ambiente

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

# 4. Instalar dependências

pip install -r requirements.txt


# 5. Executar

python LGPD.py


---

## Funcionalidades

## Atividade 2

* Anonimiza dados (nome, cpf, email, telefone)
* Gera arquivos CSV por ano de nascimento

## Atividade 3

* Gera arquivo `todos.csv`
* Contém nome e cpf sem anonimização

---

### Logs

* Arquivo `execucao.log`
* Registra tempo de execução das atividades

---

#### Estrutura


Mini-Projeto-2/
├── LGPD.py
├── requirements.txt
├── README.md
├── execucao.log
└── *.csv


---

##### Requisitos

* Python 3
* Acesso ao banco PostgreSQL
