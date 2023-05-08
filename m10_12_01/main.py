from jose import jwt, JWTError

secret_key = 'b0d308ce7dfc39643ee52c2ab5efd7a5a876ae266fa4ec98efb79879232d088c'

# дані для заповнення токена
payload = {"sub": "krabat@meta.ua", "username": "Krabaton", "role": "administrator"}

# створення токена з симетричним ключем
encoded = jwt.encode(payload, secret_key, algorithm=jwt.ALGORITHMS.HS512)
print(encoded)

try:
    # перевірка токена
    decoded = jwt.decode(encoded, secret_key, algorithms=['HS256', 'HS512'])
    print(decoded)
except JWTError as e:
    print(e)