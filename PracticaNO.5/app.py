from flask import Flask 

#Estamos declarando el app y le estamos asignando un nombre
# Inicializacion del servidor flask
app= Flask(__name__)
# Configuraciones para la conexion con la BD
app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "danny22"
app.config['MYSQL_DB']= "dbflask"


# Declaramos una ruta 
# Declaramos la ruta index http://localhost:5000
# La ruta se compone del nombre y la funcion 

@app.route('/')
def index():
    return "Hola Mundo"


@app.route('/Guardar')
def guadar():
    return "Se guardo el album enla BD"


@app.route('/Eliminar')
def eliminar():
    return "Se elimino el album en la BD"

# Ejecucion 
if __name__ == '__main__':
    app.run(port= 5000, debug = True)
    