from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask !"

@app.route('/second')
def second():
    return 'İkinci Sayfaya Hoşgeldiniz !'

@app.route('/second/third')
def third():
    return 'Üçüncü Sayfaya Hoşgeldiniz'

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'Bu Sayfanın ID Numarası {id}'
    
    






if __name__ == '__main__':
    app.run(debug=True, port=2000)