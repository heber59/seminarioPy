import matplotlib.pyplot as plt
from flask import Flask, request, send_file
import io
import base64

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
       # pregunta10 = int(request.form['pregunta10'])
        #pregunta11 = int(request.form['pregunta11'])
        #pregunta12 = int(request.form['pregunta12'])
        
        nombre = request.form['nombre']
        ingenieria = (pregunta1 + pregunta2 + pregunta3 + pregunta4)
        carreras_medicina = (pregunta5 + pregunta6 + pregunta7 + pregunta8)
        sociedad_economia = (pregunta9 )
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
       # Obtener la imagen en formato base64 para mostrarla en el HTML
        img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
        img_tag = f'<img src="data:image/png;base64,{img_base64}" alt="Grafico de puntajes">'

        # Formar el HTML con la imagen y el botón
        html_response = f'''
            {img_tag}
            <button onclick="window.location.href='/estadisticas'">ver estadisticas</button>
        '''

        return html_response
@app.route('/estadisticas')
def estadisticas():
    # Lógica para mostrar las estadísticas
    # ...
    print("funciona")
    estadisticaRespuestas= f'''
    
    '''
    return estadisticaRespuestas  # Ejemplo de retorno para una página simple

if __name__ == '__main__':
    app.run(debug=True)