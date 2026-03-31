from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Roles(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(30))


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30))
    surname = db.Column(db.String(32), nullable=False)
    login = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    password = db.Column(db.String(100))
    datebirth = db.Column(db.String(12))
    last_login = db.Column(db.String(50)) 

with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_val = request.form.get('login')
        password = request.form.get('password')

        user = Users.query.filter_by(login=login_val, password=password).first()

        if user:

            user.last_login = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db.session.commit()

            return redirect(url_for('main'))  
        else:
            return "Неверный логин или пароль"

    return render_template('login.html')


@app.route('/home')
def main():
    return render_template('main.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('name')
        surname = request.form.get('surname')
        login_val = request.form.get('login')
        email = request.form.get('email')
        role_id = request.form.get('role')
        password = request.form.get('password')

        add_bd_user(
            username=username,
            surname=surname,
            login=login_val,
            email=email,
            role_id=role_id,
            password=password
        )

    return render_template('register.html')


# --- ФУНКЦИИ ДЛЯ БД ---

def add_bd_user(username, surname, login, email, role_id, password):
    user = Users(
        username=username,
        surname=surname,
        login=login,
        email=email,
        role_id=role_id,
        password=password
    )
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(e)


# --- ЗАПУСК ---

if __name__ == "__main__":
    app.run(debug=True)