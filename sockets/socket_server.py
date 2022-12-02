"""
    This program simulate a server, is listenig a request, 
    and after return to client in port 9000.
"""
import socket

print("Access: http://localhost:9000")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(("localhost", 9000))
    server_socket.listen(5)

    while True:
        (clientsocket, addres) =  server_socket.accept()

        request = clientsocket.recv(5000).decode()
        print(request, end="-----------------/n")

        response =  "HTTP\1.1 200 OK\n"
        response += "Content-type: text/html\n"
        response += "\n"
        response += "<html><body><h1>Hello World</h1></body></html>"

        clientsocket.sendall(response.encode())
        clientsocket.shutdown(socket.SHUT_WR)
except KeyboardInterrupt:
    print("Shutting down...")
except Exception as e:
    print(e)

server_socket.close()
