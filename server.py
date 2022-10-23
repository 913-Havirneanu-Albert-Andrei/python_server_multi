import threading
import socket
IP = "0.0.0.0"
PORT = 5050
BYTES = 16
ADDRESS = (IP , PORT)

#initialize server
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDRESS)


#function to execute for every new thread/client
def handleClient(client , address):
    print(f"New connection {address} connected")
    message = client.recv(BYTES).decode("utf-8") # 16 represent nr of bytes received from client
    print(message)
    client.close()


def main():
    server.listen() # listening for connections
    while True:
        client , address = server.accept()
        thread = threading.Thread(target = handleClient , args = (client , address))
        thread.start()
        print(f"Nr of connections: {threading.active_count() - 1}")


main()