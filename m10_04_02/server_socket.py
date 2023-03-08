import socket


def main():
    host = socket.gethostname()  # '127.0.0.1'
    port = 4000

    s_socket = socket.socket()
    s_socket.bind((host, port))
    s_socket.listen()

    conn, address = s_socket.accept()
    print(f"Connection from {address}")
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print(f"Received message: {msg}")
        message = input('>>> ')
        conn.send(message.encode())
    conn.close()
    s_socket.close()


if __name__ == '__main__':
    main()
