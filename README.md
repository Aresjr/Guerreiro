## Bem-vindo, Guerreiro

#### Só baixar e rodar
  ```
  $ git clone https://github.com/Aresjr/Guerreiro.git
  $ cd Guerreiro
  $ virtualenv env
  $ source env/bin/activate
  $ pip install -r requirements.txt
  $ flask run
  ```

#### Criar Base / Migration
  ```
  $ flask db init
  $ flask db migrate
  $ flask db upgrade
  ```
#### Conexão local com a base
  ```
  $ psql -h localhost -p 5432 -d guerreiro -U postgres -W
  ```

#### Carga Inicial
  ```
  $ python dataload.py
  ```

#### Documentacão API
https://app.swaggerhub.com/apis-docs/Aresjr/guerreiro/0.0.1
