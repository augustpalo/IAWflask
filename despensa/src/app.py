from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM despensa")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Ruta para guardar usuarios en la bdd
@app.route('/ingrediente', methods=['POST'])
def addUser():
    ingrediente = request.form['ingrediente']
    cantidad = request.form['cantidad']
    receta = request.form['receta']
    nevera = request.form['nevera']
    if nevera != True:
        nevera = False

    if ingrediente and cantidad and receta and receta:
        cursor = db.database.cursor()
        sql = "INSERT INTO despensa (ingrediente, cantidad, receta, nevera) VALUES (%s, %s, %s, %s)"
        data = (ingrediente, cantidad, receta, int(nevera))
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM despensa WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    ingrediente = request.form['ingrediente']
    cantidad = request.form['cantidad']
    receta = request.form['receta']

    if ingrediente and cantidad and receta:
        cursor = db.database.cursor()
        sql = "UPDATE despensa SET ingrediente = %s, cantidad = %s, receta = %s WHERE id = %s"
        data = (ingrediente, cantidad, receta, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)