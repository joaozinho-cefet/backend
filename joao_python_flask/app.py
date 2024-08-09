from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()