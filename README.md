# Mini Projeto 2 - LGPD

## Descrição
Projeto acadêmico em Python que acessa um banco PostgreSQL, aplica anonimização de dados sensíveis conforme a LGPD e gera arquivos CSV.

---

## Objetivo
Anonimizar dados pessoais e exportar:
- arquivos CSV por ano de nascimento (anonimizados)
- um arquivo único com nome e CPF sem anonimização

---

## Tecnologias
- Python 3
- SQLAlchemy
- psycopg2

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
- Anonimização de:
  - nome
  - CPF
  - email
  - telefone
- Geração de arquivos CSV por ano de nascimento

### Atividade 3
- Geração de arquivo `todos.csv`
- Contém apenas nome e CPF sem anonimização

---

## Como funciona

1. Conecta ao banco PostgreSQL  
2. Lê dados da tabela `usuarios`  
3. Aplica anonimização (LGPD)  
4. Agrupa dados por ano de nascimento  
5. Gera arquivos CSV por ano  
6. Gera arquivo único sem anonimização  

---

## Monitoramento

O projeto utiliza um decorador para medir o tempo de execução.

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
- Python 3
- Acesso ao banco PostgreSQL

---

## Autor
Felippe Santuzzi

---

## Status
Projeto acadêmico concluído