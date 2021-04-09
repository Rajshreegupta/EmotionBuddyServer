from django.shortcuts import render
from django.http import HttpResponse
import socket

# Create your views here.
class Chatting():

    def home(self, request):
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        self.conn, addr = s.accept()
        return render(request, 'home.html', {'msg_from_client':'Client connected!!!'})

    def sendmsg(self, request):
        message = request.POST["msg_from_server"]
        message = message.encode()
        self.conn.send(message)
        # print('Sent')
        # print()
        incoming_message = self.conn.recv(1024)
        incoming_message = incoming_message.decode()
        # print(' Client : ', incoming_message)
        # print()
        return render(request, 'home.html', {'msg_from_client': incoming_message})

    def receivemsg(self, request):
        incoming_message = self.conn.recv(1024)
        incoming_message = incoming_message.decode()
        # print(' Client : ', incoming_message)
        # print()
        return render(request, 'home.html', {'msg_from_client':incoming_message})