from data import db_session
from flask import Flask
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = "21"
    user.position = "captain"
    user.speciality = "research enginee"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    app.run()

    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = 'Nacist'
    user.name = 'Egor'
    user.age = 15
    user.position = 'student'
    user.speciality = 'autistic'
    user.address = 'bebelya 109'
    user.email = 'egor@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    app.run()

    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = 'Tatar'
    user.name = 'Samat'
    user.age = 16
    user.position = 'student'
    user.speciality = 'chillguy'
    user.address = 'hz 100'
    user.email = 'samat@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    app.run()

if __name__ == '__main__':
    main()
