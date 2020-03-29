import socket
import time
import threading

def socket_target_function(conn, address, i):
    data = ""
    while data!="\n":
        data = input(conn.recv(1024).decode())
        #time.sleep(2)
        print(str(data))
        conn.send(str(input()+"\n").encode())
    conn.close()





master_socket= socket.socket()
master_socket.bind(('127.0.0.1', 5001))
i=2
connections = []
master_socket.listen(i)
master_socket.setblocking(False)
while True:
    try:
        connection, address = master_socket.accept()
        print(str(address))
        connections.append(threading.Thread(target=socket_target_function, args=(connection, address, i)))
    except:
        time.sleep(1)
        continue
for i in range(len(connections)):
    connections[i].start()
for i in range(len(connections)):
    connections[i].join()
print("done")
