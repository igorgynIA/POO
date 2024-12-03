from app import app
from flask import request, render_template, redirect, url_for

@app.route("/login_adm")
def login_adm():
    return render_template("login_adm.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/inicio", methods=['POST']) 
def autentica_rest():
    nome = request.form['nome']
    senha = request.form['senha']
    return render_template('inicio.html', nome=nome, senha=senha)

funcionarios = [
    {"id": 1, "nome": "Nome: João", "cargo": "Cargo: Gerente", "salario": "Salario: R$ xxxx,xx", "banco": "Santander...", "cpf": "000.000.000-00"},
    {"id": 2, "nome": "Nome: Maria", "cargo": "Cargo: Atendente", "salario": "Salario: R$ yyyy,yy", "banco": "Inter...", "cpf": "111.111.111-11"},
]

@app.route("/funcionario", methods=["GET", "POST"])
def funcionario():
    global funcionarios  
    if request.method == "POST":
        nome = request.form.get("nome")
        cargo = request.form.get("cargo")
        salario = request.form.get("salario")
        banco = request.form.get("banco")
        cpf = request.form.get("cpf")
        funcionarios.append({"id": len(funcionarios) + 1, "nome": nome, "cargo": cargo, "salario": salario, "banco": banco, "cpf": cpf})
    return render_template("funcionario.html", funcionarios=funcionarios)

@app.route("/adicionar_funcionario") 
def adicionar_funcionario():
    nome = request.form.get('nome')
    return render_template("adicionar_funcionario.html")


@app.route("/remove_funcionario/<int:id>", methods=["POST"])
def remove_funcionario(id):
    global funcionarios
    funcionarios = [f for f in funcionarios if f["id"] != id]
    return redirect(url_for("funcionario"))

@app.route("/editar_funcionario/<int:id>", methods=["GET", "POST"])
def editar_funcionario(id):
    global funcionarios
    # Busca o funcionário pelo ID
    funcionario = next((f for f in funcionarios if f["id"] == id), None)
    if not funcionario:
        return "Funcionário não encontrado!", 404

    if request.method == "POST":
        # Atualiza os dados do funcionário
        funcionario["nome"] = request.form.get("nome")
        funcionario["cargo"] = request.form.get("cargo")
        funcionario["salario"] = request.form.get("salario")
        funcionario["banco"] = request.form.get("banco")
        funcionario["cpf"] = request.form.get("cpf")
        return redirect(url_for("funcionario"))

    # Renderiza o template de edição com os dados do funcionário
    return render_template("editar_funcionario.html", funcionario=funcionario)

@app.route("/cadastro_rest")
def cadastro_rest():
    return render_template("cadastro_rest.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html", itens=itens_cardapio)

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

@app.route("/pedidos") 
def pedidos():
    return render_template("pedidos.html")

@app.route("/restaurante", methods=['POST']) 
def cadastrar_rest():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    cnpj = request.form['cnpj']
    return render_template('login_adm.html', nome=nome, email=email, telefone=telefone,senha=senha, cnpj=cnpj)

@app.route("/adicionar_item") 
def adicionar_item():
    return render_template("adicionar_item.html")
