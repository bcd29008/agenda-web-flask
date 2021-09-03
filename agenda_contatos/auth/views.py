import functools

from flask import Blueprint, render_template, session, redirect, url_for, flash, g

from werkzeug.security import check_password_hash

from agenda_contatos.auth.forms import LoginForm
from agenda_contatos.extensions.database import db

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='../static', static_url_path='assets')

@auth_bp.route('/',methods=['GET', 'POST'])
def autenticar():
    if session.get('idUsuario') is not None:
        return redirect(url_for('home_bp.inicio'))
    form = LoginForm()
    # Entra no IF quando a requisição vier via POST
    if form.validate_on_submit():
        # Faz a autenticação do usuário e senha
        usuario = db.conn.session.query(db.Usuario).filter(db.Usuario.username == form.username.data).first()
        if usuario:
            if check_password_hash(usuario.password, form.password.data):
                session['nome'] = usuario.nome
                session['idUsuario'] = usuario.idUsuario
                return redirect(url_for('home_bp.inicio'))
        flash('Usuário ou senha inválidos')
        return redirect('/')
    return render_template('auth/login.html', title='Autenticação de usuários', form=form)

def login_required(view):
    """
    Criação de um novo decorator para ser usado em todas as rotas e assim garantir
    que o usuário deverá estar autenticado para acessar algumas rotas.
    :return: a view solicitado se o usuário estiver autenticado, caso contrário a view com o formulário de login
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('idUsuario') is None:
            return redirect(url_for('auth_bp.autenticar'))
        return view(**kwargs)
    return wrapped_view


@auth_bp.route('/logout',methods=['GET'])
def logout():
    '''
    Para encerrar a sessão autenticada de um usuário
    :return: redireciona para a página inicial
    '''
    session.clear()
    return redirect(url_for('home_bp.inicio'))