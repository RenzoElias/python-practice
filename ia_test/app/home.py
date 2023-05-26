from flask import Blueprint, render_template


bp = Blueprint('home', __name__,template_folder='templates')

# Ruta inicial
@bp.route('/')
@bp.route('/home')
def index():
    return render_template('index.html')