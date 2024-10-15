from pony.orm import DataBase, Required, PrimaryKey, Optional
import datetime

db = DataBase()

class LogEventos(db.Entity):
    id = PrimaryKey(int, auto = True)
    descricao = Optional(str)
    tipo = Optional(str)
    data_criacao = optional(datetime.datetime, default = datetime.datetime.now)
    usuario = Optional(str)

class Usuario(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = required(str, unique=True)
    hashed_password = Required(str)

db.bind(provider='sqlite', filename = 'database.sqlite', create_db=True)
db.generate_mapping(create_tables=Trues)