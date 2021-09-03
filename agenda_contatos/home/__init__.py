from flask import current_app as app
from flask_nav.elements import View, Subgroup


@app.before_first_request
def before_first_request():
    """
    Esse menu será criado antes do primeiro pedido quando o usuário já estiver passado pela autenticação.
    """
    app.menubar.items.append(View('Início', 'home_bp.inicio'))
    app.menubar.items.append(Subgroup('Contatos', View('Cadastrar', 'contato_bp.cadastrar_contato'), View('Listar', 'contato_bp.listar')))
    app.menubar.items.append(Subgroup('Grupos', View('Cadastrar', 'grupo_bp.cadastrar'), View('Listar', 'grupo_bp.listar')))
    app.menubar.items.append(View('Sair', 'auth_bp.logout'))