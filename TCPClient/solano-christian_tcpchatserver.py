from socket import *

serverPort = 6969

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(1)

print "Chat is ready"

while 1:

     connectionSocket, addr = serverSocket.accept()

     sentence = connectionSocket.recv(1024)
     print "User B responds: %r" %(sentence)
     
     yourinput = raw_input("chat input:")
     if yourinput == 'Quit':
          break
     else:
          connectionSocket.send(yourinput)

          connectionSocket.close()
