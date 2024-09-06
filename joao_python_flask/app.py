from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Projeto
app.config['SECRET_KEY'] = 'HASH-HASH-INVASOR_FDP@ablebleblebel_kshg**fiekn67gfsgfhVASHfvjÇShfvjsçfbJH'


# drive://usuario:senha@servidor/banco_de_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/projeto"
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

@app.route('/projeto')
def projeto():
    u = Projeto.query.all()
    return render_template('usuario_lista.html', dados = u)

@app.route('/projeto/add')
def projeto_add():
    return render_template('usuario_add.html')

@app.route('/projeto/save', methods=['POST'])
def projeto_save():
    nome =request.form.get('nome')
    data_i =request.form.get('data_i')
    data_f =request.form.get('data_f')
    if nome and data_i and data_f:
        projeto = Projeto(nome, data_i, data_f)
        db.session.add(projeto)
        db.session.commit()
        flash("Projeto cadastrado com suscesso!!!")
        return redirect('/projeto/add')
    else:
        flash("Preencha Todos os Campos Corretamente!!!")
        return redirect('/projeto/add')

@app.route('/projeto/remove/<int:id>')
def projeto_remove(id):
    projeto = Projeto.query.get(id)
    if id > 0:
        db.session.delete(projeto)
        db.session.commit()
        flash('usuario removido com suscesso!!!')
        return redirect('/projeto')
    else:
        flash('Caminho incorreto!!!')
        return redirect('/projeto')
    
@app.route('/projeto/edita/<int:id>')
def projeto_edita(id):
    projeto = Projeto.query.get(id)
    return render_template('projeto_edita.html', dados = projeto)

@app.route('/projeto/editasave', methods=['POST'])
def projeto_editasave():
     nome =request.form.get('nome')
     data_i =request.form.get('data_i')
     data_f =request.form.get('data_f')
     id =request.form.get('id')
     if id and nome and data_i and data_f:
         projeto = Projeto.query.get(id)
         projeto.nome = nome
         projeto.data_i = data_i
         projeto.data_f = data_f
         db.session.commit()
         flash("Dados atualizados!")
         return redirect('/projeto')
     else:
         flash('Faltando dados')
         return redirect('/projeto')
         

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