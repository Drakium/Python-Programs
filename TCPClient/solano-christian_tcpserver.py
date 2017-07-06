from socket import *

serverPort = 6969

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(1)

print "Server is ready"

while 1:

     connectionSocket, addr = serverSocket.accept()

     sentence = connectionSocket.recv(1024)

     capitalizedSentence = sentence.upper()

     connectionSocket.send(capitalizedSentence)

     connectionSocket.close()
     
