from app import app
from flask import request, render_template

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/login_adm")
def login_adm():
    return render_template("login_adm.html")

@app.route("/login_cli")
def login_cli():
    return render_template("login_cli.html")

@app.route("/cadastro_cli")
def cadastro_cli():
    return render_template("cadastro_cli.html")

@app.route("/cadastro_rest")
def cadastro_rest():
    return render_template("cadastro_rest.html")

@app.route("/inicio") 
def inicio():
    return render_template("inicio.html")

@app.route("/funcionario") 
def funcionario():
    return render_template("funcionario.html")

@app.route("/cardapio") 
def cardapio():
    return render_template("cardapio.html")

@app.route("/pedidos") 
def pedidos():
    return render_template("pedidos.html")

@app.route("/cardapio_cli") 
def cardapio_cli():
    return render_template("cardapio_cli.html")

@app.route("/historico") 
def historico():
    return render_template("historico.html")

@app.route("/conta_cli") 
def conta_cli():
    return render_template("conta_cli.html")

@app.route("/preferencias_cli") 
def preferencias_cli():
    return render_template("preferencias_cli.html")

@app.route("/atualizar_dados") 
def atualizar_dados():
    return render_template("atualizar_dados.html")

@app.route("/atualizar_cliente", methods=['POST']) 
def atualizar_cli():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    return render_template('conta_cli.html', nome=nome, email=email, telefone=telefone, senha=senha)



@app.route("/cliente", methods=['POST']) 
def cadastrar_cli():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    return render_template('login_cli.html', nome=nome, email=email, telefone=telefone, senha=senha)

@app.route("/restaurante", methods=['POST']) 
def cadastrar_rest():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    cnpj = request.form['cnpj']
    return render_template('login_adm.html', nome=nome, email=email, telefone=telefone,senha=senha, cnpj=cnpj)


@app.route("/inicio_cli", methods=['POST']) 
def autentica_cli():
    nome = request.form['nome']
    senha = request.form['senha']
    return render_template('inicio_cli.html', nome=nome, senha=senha)

@app.route("/inicio", methods=['POST']) 
def autentica_rest():
    nome = request.form['nome']
    senha = request.form['senha']
    return render_template('inicio.html', nome=nome, senha=senha)

