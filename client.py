import socket

HOST = "localhost"#"34.232.109.82"  
PORT = 65432  

file = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b"Hello world")
    try:
        certificate = open(file,'wb')
        line = s.recv(1024)
        while line:
            certificate.write(line)
            line = s.recv(1024)
        print("certicate now here")
    except:
        data = input("Data para enviar ").encode()
        s.sendall(data)
        data = s.recv(1024)
        print(f"the server send {data.decode()}")
        print("End of the code all OKEY")
