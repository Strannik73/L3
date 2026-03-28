from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Unicode(30), autoincrement=True, primary_key = True)
    username = db.Column(db.Unicode(30), primary_key = False)
    surname = db.Column(db.Unicode(32), nullable = False)
    login = db.Column(db.Unicode(16), unique = True)
    email = db.Column(db.Unicode(32), unique = True)
    role = db.Column(db.Unicode(32), foreign_key = 'Roles.Role_id')
    password = db.Column(db.Unicode(100))
    datebirth = db.Column(db.Unicode(12))

class Roles(db.Model):
    role_id = db.Column(db.Integer, autoincrement=True, primary_key = True)
    role_name = db.column(db.String(30))

    def __repr__(self):
        return super().__repr__()
    
with app.app_context():
    db.creats_all
    
@app.route('/')
@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return render_template('login.html')
    
    return render_template('login.html')
    

@app.route('/home')
def main():
    return render_template('main.html')


@app.route('/register', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        login = request.form.get('login')
        email = request.form.get('email')
        role = request.form.get('role')
        password = request.form.get('password')
        add_bd_usver(name=name, surname=surname, login=login, email=email, role=role, password=password)
        return render_template('register.html')
    return render_template('register.html')

def add_bd_role():
    user = Roles(Role_name = 'usver')
    try:
        db.session.add(user)
        db.session.commit()
    except:
        print(Exception)

def add_bd_usver(name, surname, login, email, role, password, datebirth):
    user = Users(name=name, surname=surname, login=login, email=email, role=role, password=password)
    try:
        db.session.add(user)
        db.session.commit()
    except:
        print(Exception)

if __name__ == "__main__":
    app.run(debug = True)
