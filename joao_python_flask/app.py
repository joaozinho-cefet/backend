from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'HASH-HASH-INVASOR_FDP@ablebleblebel_kshg**fiekn67gfsgfhVASHfvjÇShfvjsçfbJH'

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