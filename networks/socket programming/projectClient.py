from socket import *

serverName = '94.54.174.149'
serverPort = 15000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# sunucudan ilk mesajı alıyoruz
welcomeMsg = clientSocket.recv(1024)
print(welcomeMsg.decode())

# ismimizi gönderiyoruz
name = input()
clientSocket.send(name.encode())

# soruyu alıyoruz
question = clientSocket.recv(1024)
print(question.decode())

# cevabımızı gönderiyoruz
answer = input()
clientSocket.send(answer.encode())

# sunucudan doğru ya da yanlış diye cevap geliyor
result = clientSocket.recv(1024)
print(result.decode())

clientSocket.close()
