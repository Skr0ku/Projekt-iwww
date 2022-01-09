import os
from models import *
from flask import Flask, render_template, jsonify, request, redirect 

app = Flask(__name__, template_folder='./templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:////{os.path.join(os.path.abspath('.'), 'TestDB.sqlite3')}"
db.init_app(app)


@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'GET':
        data = get_all_messages()
        return render_template('noticeboard.html', content=data)
    
    elif request.method == 'POST':
        print('tutaj powinno być obsługa dodawania nowego ogłoszenia')    


@app.route('/messages/create', methods=['POST', 'GET'])
def message_create():
    if request.method == 'GET':
        return render_template('form.html')
    
    if request.method == 'POST':
        print('tutaj powinno być obsługa dodawania nowego ogłoszenia')
        return redirect('/messages')


@app.route('/messages/<id>', methods=['GET', 'PUT', 'DELETE'])
def message(id: int):
    if request.method == 'GET':
        message = f'treść ogłoszenie nr {id}'
        data = get_message_details(id=id)
        
    if request.method == 'PUT':
        message = f'aktualizacja ogłoszenia nr {id}'
    
    if request.method == 'DELETE':
        message = f'usunięcie ogłoszenie nr {id}'

    content = {'id': id, 'message': message, 'data': data}
    return render_template('details.html', content=content)

@app.route('/test', methods=['GET'])
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=False)