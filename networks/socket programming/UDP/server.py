from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('Sunucu hazir bekliyor')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Yeni istemci mesaj gonderdi')
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
    print('İstemciye cevap gonderildi')
