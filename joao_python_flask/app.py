from flask import Flask, render_template, request, flash
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Usuario
app.config['SECRET_KEY'] = 'HASH-HASH-INVASOR_FDP@ablebleblebel_kshg**fiekn67gfsgfhVASHfvjÇShfvjsçfbJH'


# drive://usuario:senha@servidor/banco_de_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/Projeto"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aulasinha')
@app.route('/aulasinha/<nome>')
@app.route('/aulasinha/<nome>/<curso>')
@app.route('/aulasinha/<nome>/<curso>/<int:ano>')
def aulinha(nome = 'João', curso = 'Informática', ano = 2):
    dados = {'nome':nome,'curso':curso, 'ano':ano}
    return render_template('aulasinha.html', dados_curso=dados)

@app.route('/usuario')
def usuario():
    u = Usuario.query.all()
    return render_template('usuario_lista.html', dados = u)



@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados',methods=['POST'])
def dados():
    flash('Dados enviados')
    dados = request.form
    return render_template('dados.html', dados=dados)


if __name__ == '__main__':
    app.run()