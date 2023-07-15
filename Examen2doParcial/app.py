from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL

app= Flask(__name__)
# Configuraciones para la conexion con la BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "danny22"
app.config['MYSQL_DB']= "bd_floreria"

app.secret_key= 'mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('menu.html')    

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/insertar', methods=['POST'])
def insertar():
    if request.method == 'POST':
        vflor= request.form['txtFlor']
        vcantidad= request.form['txtCantidad']
        vprecio= request.form['txtPrecio']
    
        CS= mysql.connection.cursor()
        CS.execute('insert into tbflores(Nombre, cantidad, precio) values(%s, %s, %s)',(vflor, vcantidad, vprecio))
        mysql.connection.commit()
    flash('Registro agregado Correctamente')    
    return redirect(url_for('formulario'))
       


    



if __name__ == '__main__':
    app.run(port= 8000, debug = True)