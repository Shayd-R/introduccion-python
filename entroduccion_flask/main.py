from flask import Flask, render_template
#render_template=>es para ver lo de las plantillas y esta busca siempre la carpeta template
app=Flask(__name__)

@app.get("/")#ruta de inicio
def inicio():
    #return "<h1>Hola mundo</h1>"
    return render_template("index.html")

@app.get("/contactos")
def listaContactos():
    return render_template("contactos.html")

#@app.get("/contactos/contactoId")#quiere decir toca buscarla por esta ruta
@app.get("/contactos/<int:contactoId>")#quiere decir que es una ruta dinamica de enteros nada mas
#@app.get("/contactos/<contactoId>")#quiere decir que es una ruta dinamica
def EditarContacto(contactoId):
    return render_template("editarContactos.html")#str es para pasar de un entero a string

app.run(debug=True)