import socket
import ssl

HOST = "192.168.1.94"  
PORT = 65432 


context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.verify_mode = ssl.CERT_OPTIONAL 
context.check_hostname = False
context.load_verify_locations(cafile="certs\ca.crt")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.connect((HOST,PORT))
        ssock.sendall(b"Hola mundo")
        data = ssock.recv(1024)

print(data.decode())

# 34.232.109.82

