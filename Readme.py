# Mini Projeto 2 - LGPD

## Descrição

Projeto acadêmico desenvolvido em Python para aplicar conceitos da LGPD. O sistema acessa um banco de dados PostgreSQL, realiza anonimização de dados sensíveis e gera arquivos CSV organizados.

---

## Objetivo

Anonimizar dados pessoais e exportar informações organizadas por ano de nascimento, além de gerar um arquivo consolidado sem anonimização.

---

## Tecnologias

* Python 3
* SQLAlchemy
* psycopg2

---

## Execução

### 1. Clonar repositório

```bash
git clone <url-do-repositorio>
cd Mini-Projeto-2
```

### 2. Criar ambiente virtual

```bash
python3 -m venv venv
```

### 3. Ativar ambiente

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o projeto

```bash
python LGPD.py
```

---

## Funcionalidades

### Atividade 2

* Anonimização de dados:

  * Nome
  * CPF
  * Email
  * Telefone
* Geração de arquivos CSV por ano de nascimento

### Atividade 3

* Geração de arquivo único `todos.csv`
* Contém apenas nome e CPF sem anonimização

---

## Como funciona

1. Conecta ao banco PostgreSQL
2. Lê dados da tabela `usuarios`
3. Aplica anonimização conforme regras da LGPD
4. Agrupa os dados por ano de nascimento
5. Gera arquivos CSV por ano
6. Gera arquivo consolidado sem anonimização

---

## Monitoramento

O projeto utiliza um decorador para medir o tempo de execução das atividades e registrar os resultados em log.

Arquivo gerado:

```
execucao.log
```

---

## Estrutura do projeto

```
Mini-Projeto-2/
├── LGPD.py
├── requirements.txt
├── README.md
├── execucao.log
└── *.csv
```

---

## Requisitos

* Python 3
* Acesso ao banco PostgreSQL

---

## Autor/Supervisão

Felippe Santuzzi
    Professor: Orlando Saraiva

---

## Status

Mini projeto acadêmico concluído.
