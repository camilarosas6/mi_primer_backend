from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

usuario = {
    'email': 'ejemplo@gmail.com',
    'password' : '123456'
}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/success', methods=['post'])
def success():
    email = request.form['email']
    password = request.form['password']
    print (email, password)
    if email == usuario['email'] and password == usuario['password']:
        return render_template('success.html')
    
    else:
        print("no :( )")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)