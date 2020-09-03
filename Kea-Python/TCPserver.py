from socket import*
serverPort =12042 #Lav om til port 80
serverSocket = socket(AF_INET, SOCK_STREAM)
try:
    serverSocket.bind(("", serverPort))
except:
    serverPort += 1
    serverSocket.bind(("", serverPort))
    serverSocket.listen(1)
print ("The server is ready to receive " + serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()