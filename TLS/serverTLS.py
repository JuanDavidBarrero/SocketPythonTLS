import socket
import ssl

HOST = "localhost"  
PORT = 65432  


context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("./certs/certificate.crt", "./certs/key.pem")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('0.0.0.0', PORT))
    sock.listen()
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print(F"Conectado de {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                text = F"data desde el servidor {data.decode()} TLS 1.2"
                conn.sendall(text.encode())
    