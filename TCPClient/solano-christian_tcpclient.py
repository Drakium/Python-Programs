from socket import *

serverName = 'localhost'

serverPort = 6969
while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverName,serverPort))
    sentence = raw_input("Please input a sentence:")

    clientSocket.send(sentence)

    modifiedSentence = clientSocket.recv(1024)
    if modifiedSentence == 'QUIT':
        break
    else:
        print "test input: %r" %(modifiedSentence)

