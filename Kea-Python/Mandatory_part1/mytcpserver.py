#! /usr/bin/python3

from socket import *
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
isnotbound = True
while isnotbound:
    try: 
        serverSocket.bind(('', serverPort))
        isnotbound = False
    except:
        serverPort += 1
        print(serverPort)
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(1024).decode()
    headers = request.split('\r\n')
    with open("log.txt", "a") as mylog:
        mylog.write("--------------------\n")
        for i in headers:
            mylog.write(i + "\n")
        
    try: 
        requestLine = headers[0]
        val = requestLine.split(" ")
        requestedFile = str(val[1][1:])
        if(requestedFile == '/' or requestedFile == ''):
            requestedFile = 'index.html'
        print("File", requestedFile, type(requestedFile))
        file1 = open(requestedFile,'rb')
        response = file1.read()
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" #Connection: keep-alive\r\nTransfer Encoding: chunked\r\n"
    except IOError:
        print("404")
        header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n" # Content-Type: text/html\r\nConnection: keep-alive\r\n
        response = '<html><body><p>Error 404: File not found</p></body></html>\r\n'.encode("utf-8")
    except Exception as e:
        print(e) 
        print("400")
        header = "HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n" #Content-Type: text/html\r\nConnection: keep-alive\r\n
        response = '<html><body><p>Error 400: Bad Request</p></body></html>'.encode("utf-8")
    finally:
        final_response = header.encode("utf-8") + response
        connectionSocket.send(final_response) 
        print("Closing")
        connectionSocket.close()

