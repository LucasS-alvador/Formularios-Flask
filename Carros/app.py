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

@app.route("/adicionar_carro", methods=["POST"])
def adicionar_carro():

    # ---- Velho -----
    # marca = request.args.get("marca")
    # modelo = request.args.get("modelo")
    # ano = request.args.get("ano")
    # quilometros = request.args.get("quilometros")
    # disponivel = request.args.get("disponivel")
    # preco = request.args.get("preco")
    # cor = request.args.get("cor")
    # dataRevisao = request.args.get("dataRevisao")
    # placa = request.args.get("placa")
    # numeroPortas = request.args.get("numeroPortas")

    # with db_session:
    #     c = Carro(**request.args)
    #     commit()
    #     return redirect("listar_carros")

    # ---- Novo 0.1 -----
    # with db_session:
    #     marca = request.args.get("marca")
    #     modelo = request.args.get("modelo")
    #     ano = request.args.get("ano")
    #     quilometros = request.args.get("quilometros")
    #     disponivel = request.args.get("disponivel") == "True"
    #     preco = request.args.get("preco")
    #     cor = request.args.get("cor")
    #     dataRevisao = request.args.get("dataRevisao")
    #     placa = request.args.get("placa")
    #     numeroPortas = request.args.get("numeroPortas")
    #     c = Carro(
    #         marca=marca,
    #         modelo=modelo,
    #         ano=ano,
    #         quilometros=quilometros,
    #         disponivel=disponivel,
    #         preco=preco,
    #         cor=cor,
    #         dataRevisao=dataRevisao,
    #         placa=placa,
    #         numeroPortas=numeroPortas
    #     )
    #     commit()
    #     return redirect("listar_carros") 

    # ---- Novo 0.2 -----
    with db_session:
        c = Carro(
            marca=request.form.get("marca"),
            modelo=request.form.get("modelo"),
            ano=int(request.form.get("ano")),
            quilometros=int(request.form.get("quilometros")),
            disponivel=request.form.get("disponivel") == "True",
            preco=float(request.form.get("preco")),
            cor=request.form.get("cor"),
            dataRevisao=request.form.get("dataRevisao"),
            placa=request.form.get("placa"),
            numeroPortas=int(request.form.get("numeroPortas")),
        )

        commit()
        return redirect("listar_carros")

app.run(debug=True)
'''
run:
$ flask run
'''