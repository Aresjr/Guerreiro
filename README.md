[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Bem-vindo, Guerreiro

#### Só baixar e rodar
  ```
  $ git clone https://github.com/Aresjr/Guerreiro.git
  $ cd Guerreiro
  $ pip install virtualenv
  $ virtualenv env
[Linux]     $ source env/bin/activate
[Windows]   env/Scripts/activate.bat
  $ pip install -r requirements.txt
  $ flask run
  ```

#### Criar Base / Migration
  ```
  $ python migrate.py db init
  $ python migrate.py db migrate
  $ python migrate.py db upgrade
  ```
#### Conexão local com a base
  ```
  [PostgreSQL] $ psql -h localhost -p 5432 -d guerreiro -U postgres -W
  ```

#### Documentacão API
https://app.swaggerhub.com/apis-docs/Aresjr/guerreiro/0.0.1
