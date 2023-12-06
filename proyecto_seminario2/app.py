import matplotlib.pyplot as plt
from flask import Flask, request, send_file
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingenieria = int(0)
        pregunta1 = int(request.form['pregunta1'])
        pregunta2 = int(request.form['pregunta2'])
        pregunta3 = int(request.form['pregunta3'])
        pregunta4 = int(request.form['pregunta4'])
        carreras_medicina = int(0)
        pregunta5 = int(request.form['pregunta5'])
        pregunta6 = int(request.form['pregunta6'])
        pregunta7 = int(request.form['pregunta7'])
        pregunta8 = int(request.form['pregunta8'])
        sociedad_economia = int(0)
        pregunta9 = int(request.form['pregunta9'])
        pregunta10 = int(request.form['pregunta10'])
        pregunta11 = int(request.form['pregunta11'])
        pregunta12 = int(request.form['pregunta12'])

        nombre = request.form['nombre']
        ingenieria = (pregunta1 + pregunta2 + pregunta3 + pregunta4)
        carreras_medicina = (pregunta5 + pregunta6 + pregunta7 + pregunta8)
        sociedad_economia = (pregunta9 + pregunta10 + pregunta11 + pregunta12)
        puntajes = [ingenieria, carreras_medicina, sociedad_economia]
        areas = ['Ingeniería', 'Carreras de Medicina', 'Sociedad/Economía']

        plt.figure(figsize=(8, 6))
        plt.bar(areas, puntajes, color='skyblue')
        plt.title('Puntajes por área de interés')
        plt.xlabel('Área de interés')
        plt.ylabel('Puntaje')
        plt.ylim(0, max(puntajes) + 10)  # Ajusta el rango del eje y si es necesario
        plt.grid(axis='y')  # Agrega una cuadrícula en el eje y
        plt.tight_layout()

        # Guardar el gráfico como un archivo en memoria
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        # Mostrar el gráfico al usuario
        return send_file(img, mimetype='image/png')

    return '''
        <form method="post">
            <!-- Aquí van tus campos de formulario -->
            <input type="text" name="nombre" placeholder="Nombre"><br><br>
            <!-- Agrega los campos restantes aquí -->
            <button type="submit">Enviar</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)