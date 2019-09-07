import socket

host=socket.gethostname()
port=(8000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def connect():
    s.bind((host,port))
    s.listen(2)
    print("Server listening")
    conn,addr=s.accept()
    print("Connected")
    send(conn)

# def receive(conn):
#   while 1:
#       try:
#       data=conn.recv(1024)
#       decoded_data=data.decode('UTF-8')
#       if not decoded_data:
#           print("No data")
#       else:
#           print("New data")
#           print(decoded_data)

def send(conn):
    while 1:
        data=input("Input data to send: ")
        encoded_data=data.encode('UTF-8')
        conn.send(encoded_data)
connect()