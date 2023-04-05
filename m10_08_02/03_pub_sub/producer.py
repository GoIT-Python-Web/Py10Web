import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='events', exchange_type='fanout')

message = b'Danger! Attention!'
channel.basic_publish(exchange='events', routing_key='', body=message)
print(f" [x] Sent {message}")
connection.close()
