from app import app
from flask import request, render_template

@app.route("/admin") 
def homeAdmin():
    return render_template('admin.html', par1="Boa tarde", par2="Administrador do Sistema.")


# @app.route("/caminho", methods=['POST']) 
# def funcao():
