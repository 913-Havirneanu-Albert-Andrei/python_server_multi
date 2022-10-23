import socket

# FA SERVERU PE VM


IP = "192.168.0.183" # ip ul de la vm. scrii in terminal ip a
PORT = 5050 # orice port de 4 cifre should work
ADDRESS = (IP , PORT)
BYTES = 16

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDRESS)

def sendMessageToServer(message):
    message = message.encode("utf-8")
    client.send(message)

def main():
    msg = input("Message: ")
    sendMessageToServer(msg)
    client.close()

main()