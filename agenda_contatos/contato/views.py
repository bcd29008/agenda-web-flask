from datetime import datetime, date

from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify

from agenda_contatos.auth.views import login_required
from agenda_contatos.contato.forms import ContatoForm
from agenda_contatos.extensions.database import db

contato_bp = Blueprint('contato_bp', __name__, template_folder='templates', static_folder='../static', static_url_path='assets')


@contato_bp.route('/',methods=['GET', 'POST'])
@login_required
def listar():
    if request.method == 'GET':
        form = ContatoForm()
        id_usuario = session.get('idUsuario')
        contatos = db.conn.session.query(db.Contato).filter(db.Contato.idUsuario == id_usuario).all()
        return render_template('contato/listar.html', contatos=contatos, form=form)
    elif request.method == 'POST':
        id_usuario = session.get('idUsuario')
        id_contato = int(request.form['id'])
        # https://docs.sqlalchemy.org/en/14/orm/tutorial.html#common-filter-operators
        contato = db.conn.session.query(db.Contato).filter(db.Contato.idUsuario == id_usuario, db.Contato.idContato == id_contato).first()

        contado_dict = dict()
        contado_dict['id'] = contato.idContato
        contado_dict['nome'] = contato.nome
        contado_dict['dataNasc'] = contato.dataNasc.strftime('%d/%m/%Y')

        return jsonify(contado_dict)

@contato_bp.route('/atualizar',methods=['POST'])
@login_required
def atualizar_contato():
    id_usuario = session.get('idUsuario')
    id_contato = request.form['idContato']
    nome = request.form['nome']
    dataNasc = request.form['dataNasc']

    contato = db.conn.session.query(db.Contato).filter(db.Contato.idUsuario == id_usuario, db.Contato.idContato == id_contato).first()

    contato.nome = nome
    abc = datetime.strptime(dataNasc, '%d/%m/%Y').date()
    contato.dataNasc = abc.strftime('%Y-%m-%d')

    db.conn.session.commit()
    return redirect(url_for('contato_bp.listar'))

@contato_bp.route('/cadastrar',methods=['GET','POST'])
@login_required
def cadastrar_contato():
    form = ContatoForm()
    # Entra no IF somente se vier via POST
    if form.validate_on_submit():

        contato = db.Contato()
        contato.nome = form['nome'].data
        contato.dataNasc = form['dataNasc'].data.strftime('%Y-%m-%d')
        contato.idUsuario = session.get('idUsuario')

        db.conn.session.add(contato)

        for id_grupo in form['grupo'].data:
            membro_grupo = db.MembroGrupo()
            membro_grupo.contato = contato
            membro_grupo.Contato_idUsuario = session.get('idUsuario')
            membro_grupo.Grupo_idGrupo = int(id_grupo)
            membro_grupo.ingresso = date.today()
            contato.membrogrupo_collection.append(membro_grupo)

        db.conn.session.commit()

        return redirect(url_for('contato_bp.listar'))
    return render_template('contato/cadastrar.html', title='Cadastrar contato', form=form)