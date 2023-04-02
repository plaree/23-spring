from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Kucuk harfli mesajını yaz: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print ('Sunucudan cevap geldi: ', modifiedMessage.decode())
clientSocket.close()
