from flask import Blueprint, render_template
from agenda_contatos.auth.views import login_required

grupo_bp = Blueprint('grupo_bp', __name__, template_folder='templates', static_folder='../static', static_url_path='assets')

@grupo_bp.route('/')
@login_required
def listar():
    return render_template('grupo/listar.html', title='Grupos')


@grupo_bp.route('/cadastrar/')
@login_required
def cadastrar():
    return render_template('grupo/cadastrar.html', title='Cadastrar grupo')
