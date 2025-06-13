from config import *
from model import *


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_carros")
def listar_carros():
    with db_session:
        carros = Carro.select() 
        return render_template("listar_carros.html", carros=carros)

@app.route("/form_adicionar_carro")
def form_adicionar_carro():
    return render_template("form_adicionar_carro.html")

@app.route("/adicionar_carro")
def adicionar_carro():
    marca = request.args.get("marca")
    modelo = request.args.get("modelo")
    ano = request.args.get("ano")
    quilometros = request.args.get("quilometros")
    disponivel = request.args.get("disponivel")
    preco = request.args.get("preco")
    cor = request.args.get("cor")
    dataRevisao = request.args.get("dataRevisao")
    placa = request.args.get("placa")
    numeroPortas = request.args.get("numeroPortas")

    with db_session:
        c = Carro(**request.args)
        commit()
        return redirect("listar_carros") 
app.run(debug=True)
'''
run:
$ flask run
'''