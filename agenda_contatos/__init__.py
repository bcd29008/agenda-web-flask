from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar

# https://fontawesome.com/icons
from flask_fontawesome import FontAwesome

def init_app():
    '''Criando aplicação Flask'''
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        register_blueprints(app)
        initialize_extensions(app)
        register_error_handlers(app)
        return app

def register_blueprints(app):
    from .home.views import home_bp
    from .auth.views import auth_bp
    from .contato.views import contato_bp
    from .grupo.views import grupo_bp

    # Registrando os Blueprint
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth/')
    app.register_blueprint(contato_bp, url_prefix='/contato/')
    app.register_blueprint(grupo_bp, url_prefix='/grupo/')

def initialize_extensions(app):
    Bootstrap(app)
    FontAwesome(app)
    nav = Nav()
    nav.init_app(app)
    app.menubar = Navbar('Agenda de contatos')
    nav.register_element('menubar', app.menubar)


def register_error_handlers(app):
    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404


