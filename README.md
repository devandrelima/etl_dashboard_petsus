# ETL para dashboard com informações das UBSs

### Bibliotecas pra instalar

```
pip install pandas sqlalchemy psycopg2
```

### Execução

- Coloque o .csv no mesmo diretório do main.py

- Troque o nome do arquivo 'Planilha - Extração de Determinantes sociais  - Cópia de Página1.csv' para 'dados.csv'

- Sempre der drop no banco de dados quando colocar um .csv atualizado

```SQL
DROP DATABASE dashpetsus
```

- Crie o banco de dados

```SQL
CREATE DATABASE dashpetsus
```

- Rode o SQL que está no diretório sql/bd.sql

- Rode o main.py (execute via IDE ou Terminal)

```
python main.py
```

