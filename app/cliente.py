from app import app
from flask import request, render_template

@app.route("/") 
def home():
    return render_template('homepage.html')

@app.route("/login")
def login():
    return render_template("login_adm.html")

@app.route("/signin") 
def signin():
    return render_template("formCli.html")

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

@app.route("/autentica", methods=['POST']) 
def autentica():
    user = request.form['user']
    password = request.form['pswrd']
    return render_template('usuario.html', user=user, password=password)

@app.route("/cadastrarCli", methods=['POST']) 
def cadastra():
    name = request.form['name']
    cpf = request.form['cpf']
    user = request.form['user']
    password = request.form['pswrd']
    return render_template('usuario.html', name=name, cpf=cpf, user=user,password=password)