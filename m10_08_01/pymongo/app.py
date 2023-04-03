import argparse
from functools import wraps
from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://userweb10:password@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority",
                     server_api=ServerApi('1'))
db = client.web10

parser = argparse.ArgumentParser(description='Cats APP')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
name = my_arg.get('name')
age = my_arg.get('age')
_id = my_arg.get('id')
features = my_arg.get('features')


class ValidationError(Exception):
    pass


def validate(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            if arg is None:
                raise ValidationError(f'Вхідні данні не валідні: {func.__name__}{args}')
        r = func(*args)
        return r
    return wrapper


def find_cats():
    return db.cats.find()


@validate
def find_cat(uuid):
    return db.cats.find_one({"_id": ObjectId(uuid)})


@validate
def create_cat(name: str, age: int, features: list[str]):
    result = db.cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })
    return find_cat(result.inserted_id)


@validate
def update_cat(uuid: str, name: str, age: int, features: list[str]):
    r = db.cats.update_one({"_id": ObjectId(uuid)}, {
       "$set": {
            "name": name,
            "age": age,
            "features": features
        }
    })
    print(r)
    return find_cat(uuid)


@validate
def remove_cat(uuid):
    r = db.cats.delete_one({"_id": ObjectId(uuid)})
    return r


def main():
    try:
        match action:
            case 'create':
                r = create_cat(name, age, features)
                print(r)
            case 'find':
                cats = find_cats()
                [print(el) for el in cats]
            case 'update':
                print(_id, name, age, features)
                r = update_cat(_id, name, age, features)
                print(r)
            case 'remove':
                r = remove_cat(_id)
                print(r)
            case _:
                print('Unknown command!')
    except ValidationError as err:
        print(err)


if __name__ == '__main__':
    main()
