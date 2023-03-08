import socket

def main():
    host = socket.gethostname()  # '127.0.0.1'
    port = 4000  # port of server

    c_socket = socket.socket()
    c_socket.connect((host, port))
    message = input('>>> ')
    while message.lower().strip() != 'exit':
        c_socket.send(message.encode())
        msg = c_socket.recv(1024).decode()
        print(f"Received message: {msg}")
        message = input('>>> ')

    c_socket.close()


if __name__ == '__main__':
    main()
