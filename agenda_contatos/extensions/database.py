from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from flask import current_app

class Database():
    def __init__(self):
        self.conn = SQLAlchemy()
        self.conn.init_app(current_app)
        Base = automap_base()
        Base.prepare(self.conn.engine, reflect=True)

        # Para listar as classes mapeadas
        # for class_ in Base.classes:
        #     current_app.logger.info(class_)

        self.Usuario = Base.classes.Usuario
        self.Contato = Base.classes.Contato
        self.Telefone = Base.classes.Telefone
        self.Grupo = Base.classes.Grupo
        self.MembroGrupo = Base.classes.MembroGrupo

db = Database()
