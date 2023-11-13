from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def hola():
    user = ""
    password = ""
    if (request.method == "POST"):
        user = request.form.get("user")
        password = request.form.get("password")
        print("El usuario es:\t" + user + "\ncon contraseña:\t" + password)
    return render_template("index.html", user=user, password=password)

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