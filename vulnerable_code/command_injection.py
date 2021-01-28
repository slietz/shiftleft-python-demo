import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)


app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')

@app.route('/')
def index():
    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)

@app.route('/menu', methods=['POST'])
def menu():
    param = request.form['suggestion']
    command = 'echo ' + param + ' >> ' + 'menu.txt'

    subprocess.call(command, shell=True)

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)

@app.route('/clean')
def clean():
    subprocess.call('echo Menu: > menu.txt', shell=True)

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
