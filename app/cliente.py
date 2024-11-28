from app import app
from flask import request, render_template, redirect, url_for

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/login_adm")
def login_adm():
    return render_template("login_adm.html")

@app.route("/login_cli")
def login_cli():
    return render_template("login_cli.html")

@app.route("/inicio") 
def inicio():
    return render_template("inicio.html")

@app.route("/funcionario") 
def funcionario():
    return render_template("funcionario.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html", itens=itens_cardapio)

@app.route("/pedidos") 
def pedidos():
    return render_template("pedidos.html")

@app.route("/adicionar_item") 
def adicionar_item():
    return render_template("adicionar_item.html")

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

itens_cardapio = {
    "comidas": [],
    "bebidas": []
}

@app.route('/salvar_item', methods=['POST'])
def salvar_item():
    nome = request.form['nome']
    descricao = request.form['descricao']
    tipo = request.form['tipo']

    # Adicionar o item na categoria correta
    if tipo == "comida":
        itens_cardapio["comidas"].append({"nome": nome, "descricao": descricao})
    elif tipo == "bebida":
        itens_cardapio["bebidas"].append({"nome": nome, "descricao": descricao})

    # Redirecionar para a página de cardápio
    return redirect(url_for('cardapio'))
