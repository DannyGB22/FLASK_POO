from flask import Flask, render_template, request
#Estamos declarando el app y le estamos asignando un nombre
# Inicializacion del servidor flask
app= Flask(__name__)
# Configuraciones para la conexion con la BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "danny22"
app.config['MYSQL_DB']= "dbflask"
# Declaramos una ruta 
# La ruta se compone del nombre y la funcion
# Declaramos la ruta index http://localhost:5000

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method== 'POST':
        titulo= request.form['txtTitulo']
        artista= request.form['txtArtista']
        anio= request.form['txtAnio']
        print(titulo, artista, anio)
        
    return "La info del album llego a su ruta amigo;"

@app.route('/Eliminar')
def eliminar():
    return "Se elimino el album en la BD"
# Ejecucion 
if __name__ == '__main__':
    app.run(port= 5000, debug = True)
    