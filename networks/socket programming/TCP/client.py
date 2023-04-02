from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Kucuk harfli mesajini yaz: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('Sunucu cevapladi: ', modifiedSentence.decode())
clientSocket.close()
