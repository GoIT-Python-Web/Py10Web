import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError
from database.repository import get_user, get_todos, create_todo, update_todo, remove_todo

parser = argparse.ArgumentParser(description='Todo APP')
parser.add_argument('--action', help='Command: create, update, list, remove')
parser.add_argument('--id')
parser.add_argument('--title')
parser.add_argument('--desc')
parser.add_argument('--login')

arguments = parser.parse_args()
# print(arguments)
my_arg = vars(arguments)
# print(my_arg)

action = my_arg.get('action')
title = my_arg.get('title')
description = my_arg.get('desc')
_id = my_arg.get('id')
login = my_arg.get('login')


def main(user):
    match action:
        case 'create':
            create_todo(title, description, user)
        case 'list':
            todos = get_todos(user)
            for t in todos:
                print(t.id, t.title, t.description)
        case 'update':
            t = update_todo(_id, title, description, user)
            if t:
                print(t.id, t.title, t.description)
            else:
                print('Not found: 404')

        case 'remove':
            r = remove_todo(_id, user)
            print(f'Remove count: {r}')


if __name__ == '__main__':
    user = get_user(login)
    password = input('Password: ')
    if password == user.password:
        main(user)
    else:
        print('Password wrong')
