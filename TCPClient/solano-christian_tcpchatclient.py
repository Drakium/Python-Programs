from socket import *

serverName = 'localhost'

serverPort = 6969
print "Chat ready"
while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverName,serverPort))
    sentence = raw_input("chat input:")
    if sentence == 'Quit':
        break
    else:
        clientSocket.send(sentence)
    
        userAinput = clientSocket.recv(1024)
        print "User A responds: %r" %(userAinput)
