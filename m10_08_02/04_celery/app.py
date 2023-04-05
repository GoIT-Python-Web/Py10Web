from my_tasks import add


if __name__ == '__main__':
    result = add.delay(5, 2)
    print(result, result.id)
