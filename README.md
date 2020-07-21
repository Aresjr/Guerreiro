## Bem-vindo, Guerreiro

### Up and Running
  ```
  $ git clone https://github.com/Aresjr/Guerreiro.git
  $ cd Guerreiro
  $ virtualenv env
  $ source env/bin/activate
  $ pip install -r requirements.txt
  $ flask run
  ```

### Migration
  ```
  $ python migrate.py db init
  $ python migrate.py db stamp head
  $ python migrate.py db migrate
  $ python migrate.py db upgrade
  ```

### Carga Inicial
  ```
  $ python dataload.py
  ```
