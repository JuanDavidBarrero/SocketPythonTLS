import socket

HOST = "127.0.0.1"  
PORT = 65432  

file = ""

    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
                data = conn.recv(1024)
                print(f"client send {data.decode()}")
                conn.sendall(b"Hello from server")
                print("There is not file")
                if data.decode() == "END":
                    break
