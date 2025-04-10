import create_session
import global_init
from data.users import User


def main():
    db_name = input()
    global_init(db_name)
    db_sess = create_session()
    colonists = db_sess.query(User).all()
    for colonist in colonists:
        if colonist.address == "module_1":
            print(colonist)


if __name__ == '__main__':
    main()



