from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':

        numero1 = int((request.form['nota1']))
        numero2 = int((request.form['nota2']))
        numero3 = int((request.form['nota3']))
        asistencia = int((request.form['asistencia']))

        suma = numero1 + numero2 + numero3

        promedio = suma / 3

        if promedio < 40 or asistencia < 75:
            resultado = f"{promedio:.1f} <br> REPROBADO"

        else:
            resultado = f"{promedio:.1f} <br> APROBADO"

        return render_template('ejercicio1.html', resultado=resultado)

    return render_template("ejercicio1.html")




@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':

        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        nombres = [nombre1, nombre2, nombre3]
        nom_largo = max(nombres, key=len)
        caracteres = len(nom_largo)

        resultado = str(nom_largo) + str(caracteres)

        return render_template('ejercicio2.html', resultado=resultado, nom_largo=nom_largo, caracteres=caracteres)

    return render_template("ejercicio2.html")



if __name__ == '__main__':
    app.run(debug=True)