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

@app.route('/menu')
def rgmenu():
   return render_template('menu.html')

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
       

@app.route('/registros')
def registrosf():
    curSelect = mysql.connection.cursor()
    curSelect.execute('select * from tbflores')
    consulta= curSelect.fetchall()
    # print(consulta)
    return render_template('registrosform.html', listRegistro= consulta)

@app.route('/eliminar/<id>')
def eliminarf(id):
    curEliminar= mysql.connection.cursor()
    curEliminar.execute('select * from tbflores where id= %s', (id,))
    consultaID= curEliminar.fetchone()
    return render_template('eliminarRG.html', floreria = consultaID)


@app.route('/eliminarRG/<id>' , methods= ['POST'])
def eliminarRGf(id):
    if request.method == 'POST':
        CurDel = mysql.connection.cursor()
        CurDel.execute('DELETE FROM tbflores WHERE id = %s', (id,))
        mysql.connection.commit()
    flash('registro eliminado correctamente')    
    return redirect(url_for('registrosf'))


    



if __name__ == '__main__':
    app.run(port= 8000, debug = True)