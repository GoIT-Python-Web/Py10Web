import redis

client = redis.Redis(host="localhost", port=6379, password=None)

if __name__ == '__main__':
    client.set('foo', 'bar')
    client.set('num', 100)
    client.expire('num', 500)
    client.set('l', str([1, 2, 3]))

    foo = client.get('foo')
    print(foo.decode())

    num = client.get('num')
    print(int(num.decode()))

