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
  $ flask db init
  $ flask db migrate
  $ flask db upgrade
  ```

### Carga Inicial
  ```
  $ python dataload.py
  ```
