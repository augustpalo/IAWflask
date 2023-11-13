from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def hola():
    peso = 0
    altura = 0
    imc = 0
    if (request.method == "POST"):
        rango = ""
        peso = float(request.form.get("peso"))
        altura = float(request.form.get("altura"))
        imc = round(peso / (altura * altura),2)
        if imc <= 18.5:
            rango = "Bajo peso"
        elif imc > 18.5 and imc <= 24.9:
            rango = "Normal"
        elif imc > 24.9 and imc <= 29.9:
            rango = "sobrepeso"
        else:
            rango = "Obeso"
    return render_template("index.html", peso=peso, altura=altura, imc=imc, rango=rango)

@app.route("/baloncesto")
def baloncesto():
    return "Hola, esa es la web de baloncesto"

@app.route("/pruebapost", methods=["POST", "GET"])
def pruebapost():
    if (request.method == "POST"):
        return "Esto es un POST"
    elif (request.method == "GET"):
        return "Esto es un GET"
    return "Hola, esta es la prueba del post"



app.run()