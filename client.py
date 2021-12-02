import sys
from socket import *

argv = sys.argv
serverName = argv[0]
serverPort = int(argv[1])
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = argv[2]
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
print(modifiedSentence.decode())
clientSocket.close()
