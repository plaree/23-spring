from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Sunucu hazir bekliyor')
while 1:
     connectionSocket, addr = serverSocket.accept()
     print('Yeni istemci baglandi')
     sentence = connectionSocket.recv(1024)
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence)
     print('İstemciye cevap gonderildi')
     connectionSocket.close()
     print('İstemci ile baglanti sonlandirildi')
