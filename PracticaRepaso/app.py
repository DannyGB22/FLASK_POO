from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL

app= Flask(__name__)
# Configuraciones para la conexion con la BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "danny22"
app.config['MYSQL_DB']= "bd_fruteria"

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
        vfruta= request.form['txtFruta']
        vtemporada= request.form['txtTemporada']
        vprecio= request.form['txtPrecio']
        vstock= request.form['txtStock']
        
        CS= mysql.connection.cursor()
        CS.execute('insert into tbfrutas(fruta, temporada, precio, stock) values(%s, %s, %s, %s)',(vfruta, vtemporada, vprecio, vstock))
        mysql.connection.commit()
    flash('Registro agregado Correctamente')    
    return redirect(url_for('formulario'))
       

@app.route('/registros')
def registrosf():
    curSelect = mysql.connection.cursor()
    curSelect.execute('select * from tbfrutas')
    consulta= curSelect.fetchall()
    print(consulta)
    return render_template('Registros.html', listRegistro= consulta)


@app.route('/editar/<id>')
def EditarRG(id):
    curEditar= mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas where id= %s', (id,))
    consultaID= curEditar.fetchone()
    
    return render_template('EditarRG.html', register = consultaID)

@app.route('/actualizar/<id>', methods=['POST'])
def Actualizar(id):
    if request.method == 'POST':
        vfruta= request.form['txtFruta']
        vtemporada= request.form['txtTemporada']
        vprecio= request.form['txtPrecio']
        vstock= request.form['txtStock']
        CurAct = mysql.connection.cursor()
        CurAct.execute('update tbfrutas set fruta= %s, temporada =%s, precio= %s, stock=%s where id = %s', (vfruta, vtemporada, vprecio, vstock, id))
        mysql.connection.commit()
    flash('Registro Actualizado correctamente')    
    return redirect(url_for('registrosf'))


@app.route('/eliminar/<id>')
def eliminarf(id):
    curEliminar= mysql.connection.cursor()
    curEliminar.execute('select * from tbfrutas where id= %s', (id,))
    consultaID= curEliminar.fetchone()
    return render_template('eliminar.html', fruteria = consultaID)


@app.route('/eliminarRG/<id>' , methods= ['POST'])
def eliminarRGf(id):
    if request.method == 'POST':
        CurDel = mysql.connection.cursor()
        CurDel.execute('DELETE FROM tbfrutas WHERE id = %s', (id,))
        mysql.connection.commit()
    flash('registro eliminado correctamente')    
    return redirect(url_for('registrosf'))
        
    

@app.route('/consultar')
def consultar():
    return render_template('Consultar.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    if request.method == 'POST':
        fruta = request.form['txtFruta']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tbfrutas WHERE fruta = %s', (fruta,))
        consulta = cursor.fetchall()

        if consulta:
            return render_template('Consultar.html', frutas =consulta)
        else:
            flash('No se encontraron frutas con ese nombre.')

    return render_template('Consultar.html')

if __name__ == '__main__':
    app.run(port= 2000, debug = True)