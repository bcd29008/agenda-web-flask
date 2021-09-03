from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, HiddenField, validators, SelectMultipleField

from agenda_contatos.extensions.database import db


def listar_grupos():
    lista = []
    grupos = db.conn.session.query(db.Grupo).order_by(db.Grupo.nome).all()
    for g in grupos:
        lista.append((str(g.idGrupo), g.nome))
    return lista

class ContatoForm(FlaskForm):
    idContato = HiddenField('idContato')
    nome = StringField('Nome',[validators.DataRequired()])
    dataNasc = DateField('Data de nascimento',[validators.DataRequired()],format='%d/%m/%Y')
    grupo = SelectMultipleField(choices=listar_grupos())
    btnAtualizar = SubmitField('Confirmar')

