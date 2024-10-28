from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Hola, este es mi primer backend </h1>"


if __name__ == '__main__':
    app.run(debug=True)