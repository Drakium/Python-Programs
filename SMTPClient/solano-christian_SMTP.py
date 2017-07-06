#Christian Solano
#CSC 138
#Programming Project 2 SMTP Client
#Mail Client

from socket import *
import ssl
import base64


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'#Fill in start #Fill in end
mailPort = 587
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
#Fill in end
recv = clientSocket.recv(1024)
print 'testing if up to here'
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print 'test2'
print recv1
if recv1[:3] != '250':
 print '250 reply not received from server.'

startit = 'starttls\r\n'
clientSocket.send(startit)
recv1 = clientSocket.recv(1024)
print 'test2'
print recv1
if recv1[:3] != '220':
 print '250 reply not received from server.' 


clientSocketSSL = ssl.wrap_socket(clientSocket,ssl_version=ssl.PROTOCOL_SSLv23)

clientSocketSSL.send('auth login\r\n')

username = 'aeilmao@gmail.com'
clientSocketSSL.send(base64.b64encode(username) + '\r\n')
recv1 = clientSocketSSL.recv(1024)
print (recv1)
if recv1[:3] != '334':
    print('did not work.')

password = 'aeilmao123'
clientSocketSSL.send(base64.b64encode(password)+ '\r\n')
recv1 = clientSocketSSL.recv(1024)
print (recv1)
if recv1[:3] != '334':
    print('did not work.')

# Send MAIL FROM command and print server response.
testmail = 'MAIL FROM:<aeilmao@gmail.com>\r\n'
clientSocketSSL.send(testmail)
recv1 = clientSocketSSL.recv(1024)
print (recv1)
if recv1[:3] != '235':
    print('trying to work.')
    
# Send RCPT TO command and print server response.
recievemail = 'RCPT TO: <christiansol93@gmail.com>\r\n'
clientSocketSSL.send(recievemail)
recv1= clientSocketSSL.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('mail was not replyed.')

# Send DATA command and print server response.
ddd= 'DATA\r\n'
clientSocketSSL.send(ddd)
recv1 = clientSocketSSL.recv(1024)
print(recv1)
if recv1[:3] !='250':
    print ('error')
    
# Send message data.
message = raw_input('What would you like to send?: ')
messageend= '\r\n.\r\n'
# Message ends with a single period.
clientSocketSSL.send(message)
clientSocketSSL.send(messageend)
recv1 = clientSocketSSL.recv(1024)
print(recv1)
if recv1[:3] != '354':
    print ('error 2')


# Send QUIT command and get server response.
quitCommand = 'Quit\r\n'
print(quitCommand)
clientSocketSSL.send(quitCommand)
recv1 = clientSocketSSL.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('quit 250 reply not received from server.')

    pass
