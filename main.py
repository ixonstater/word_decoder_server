import socket
import json
import select
from header_interpreter import *
from decoder import *


class Server:
    def __init__(self):
        self.htmlSent = False
        self.connection = 0
        pass

    def loadFile(self):
        html_f = open('./webapp/decoder.html', 'rb')
        js_f = open('./webapp/decoder.js', 'rb')
        css_f = open('./webapp/decoder.css', 'rb')
        favicon_f = open('./webapp/ducky.ico', 'rb')
        self.html = html_f.read()
        self.js = js_f.read()
        self.css = css_f.read()
        self.favicon = favicon_f.read()
        html_f.close()
        js_f.close()
        css_f.close()
        favicon_f.close()

    def makeHeader(self):
        self.html_header = 'HTTP/1.1 200 OK\n' + 'Content Type: text/html\n\n'
        self.js_header = 'HTTP/1.1 200 OK\n' + 'Content Type: text/javascript\n\n'
        self.css_header = 'HTTP/1.1 200 OK\n' + 'Content Type: text/css\n\n'
        self.favicon_header = 'HTTP/1.1 200 OK\n' + 'Content Type: image/ico\n\n'  + 'Content Length: 432254\n\n'
        self.decoded_words_header = 'HTTP/1.1 200 OK\n' + 'Content Type: application/json\n\n'

    def makeSocket(self):
        self.portNumber = 8081
        s = socket.socket()
        s.bind(('',self.portNumber))
        s.listen(5)
        self.socket = s

    def decodeWords(self, letters):
        letters = [letter for letter in letters]
        words = vettInDictionary(generatePermutations(letters))
        response = json.dumps(words)
        return response
    
    def sendResponse(self, data):
        data = decodeRequestHeader(str(data))
        if (data == None):
            self.connection.send('HTTP/1.1 200 OK\n'.encode('utf-8'))
            return
        elif(data['Target'] == 'decoder.js'):
            response = self.js_header.encode('utf-8') + self.js
        elif(data['Target'] == 'decoder.css'):
            response = self.css_header.encode('utf-8') + self.css
        elif(data['Target'] == ''):
            response = self.html_header.encode('utf-8') + self.html
        elif(data['Target'] == 'favicon.ico'):
            response = self.favicon_header.encode('utf-8') + self.favicon
        elif (data['Target'] == None):
            response = self.decoded_words_header.encode('utf-8') + self.decodeWords(data['Body']).encode('utf-8') + '\n\n'.encode('utf-8')
        else:
            return
        self.connection.send(response)

    def serverLoop(self):
        while (True):
            connection, address = self.socket.accept()
            connection.settimeout(10)
            self.connection = connection
            try:
                data = connection.recv(4096)
            except OSError:
                print('Timed out')
            self.sendResponse(data)
            self.connection.close()


def main():
    s = Server()
    s.makeHeader()
    s.makeSocket()
    s.loadFile()    
    s.serverLoop()

if __name__ == '__main__':
    main()
