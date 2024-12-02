from app import app
from flask import request, render_template, redirect, url_for

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/login_cli")
def login_cli():
    return render_template("login_cli.html")

@app.route("/cadastro_cli")
def cadastro_cli():
    return render_template("cadastro_cli.html")

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

@app.route("/inicio_cli", methods=['POST']) 
def autentica_cli():
    nome = request.form['nome']
    senha = request.form['senha']
    return render_template('inicio_cli.html', nome=nome, senha=senha)

@app.route("/cadastrarCli", methods=['POST']) 
def cadastra():
    name = request.form['name']
    cpf = request.form['cpf']
    user = request.form['user']
    password = request.form['pswrd']
    return render_template('usuario.html', name=name, cpf=cpf, user=user,password=password)