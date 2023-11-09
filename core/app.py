from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('iindex.html')

@app.route('/captura')
def captura():
    return render_template('captura.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    imagen = request.data  # Aquí recibes la imagen capturada
    # Realiza el procesamiento de la imagen con OpenCV u otras bibliotecas

    # En este ejemplo, simplemente devolvemos un mensaje de confirmación
    return 'Imagen procesada exitosamente'

if __name__ == '__main__':
    app.run(debug=True)
