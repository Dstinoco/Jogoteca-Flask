from flask import Flask, render_template, request, redirect, session

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

  
jogo1 = Jogo('Tibia', 'MMORPG', 'PC')
jogo2 = Jogo('Counter Striker', 'FPS', 'PC')
jogo3 = Jogo('Final fantasy VII', 'RPG',  'PS1')
jogo4 = Jogo('Mortal Kombat', 'Luta', 'PS2')

lista = [jogo1, jogo2, jogo3, jogo4]

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo='Login')



@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['senha'] == 'teste':
        return redirect('/')
    else:
        return redirect('/login')
    

app.run(debug=True)