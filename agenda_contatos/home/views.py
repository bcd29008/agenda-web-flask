from flask import Blueprint, render_template, session

from agenda_contatos.auth.views import login_required

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_folder='../static', static_url_path='assets')

@home_bp.route('/')
@login_required
def inicio():
    return render_template('home/index.html', title='Inicial', usuario=session.get('nome'))
