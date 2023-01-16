import socket

HOST = "127.0.0.1"  
PORT = 65432  

file = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        print(F"data from cliente {data.decode()} \n")
        try:
            cert = open(file,'rb')
            line = cert.read(1024)
            while line:
                conn.send(line)
                line = cert.read(1024)
            cert.close()
            print("File sended successfully")
        except:
            print("There is not file")