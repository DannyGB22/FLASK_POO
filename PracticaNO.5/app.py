from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL


#Estamos declarando el app y le estamos asignando un nombre
# Inicializacion del servidor flask
app= Flask(__name__)
# Configuraciones para la conexion con la BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "danny22"
app.config['MYSQL_DB']= "dbflask"

app.secret_key= 'mysecretkey'
mysql = MySQL(app)
# Declaramos una ruta 
# La ruta se compone del nombre y la funcion
# Declaramos la ruta index http://localhost:5000

@app.route('/')
def index():
    curSelect = mysql.connection.cursor()
    curSelect.execute('select * from albums')
    consulta= curSelect.fetchall()
    print(consulta)
    
    return render_template('index.html', listAlbums = consulta)




@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method== 'POST':
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        # print(titulo, artista, anio)
        #declaramos una variable tipo curor para ejecutar los querys
        CS= mysql.connection.cursor()
        CS.execute('insert into albums(titulo, artista, anio) values(%s, %s, %s)',(Vtitulo, Vartista, Vanio))
        mysql.connection.commit()
    flash('Album Agregado correctamente')    
    return redirect(url_for('index'))

@app.route('/Eliminar')
def eliminar():
    return "Se elimino el album en la BD"



# Ejecucion 
if __name__ == '__main__':
    app.run(port= 5000, debug = True)


