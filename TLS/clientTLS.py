import socket
import ssl

HOST = ""  
PORT = 65432 

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile="./../certs/ca.pem")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.connect((HOST,PORT))
        ssock.sendall(b"Hola mundo")
        data = ssock.recv(1024)

print(data.decode())

# 34.232.109.82  cert.pem

