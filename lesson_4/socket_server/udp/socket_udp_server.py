import socketserver


class EchoUDPrHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        print('Address: {}'.format(self.client_address))
        print('Data: {}'.format(data.decode()))
        socket.sendto(data, self.client_address)


if __name__ == '__main__':
    with socketserver.UDPServer(('0', 8888), EchoUDPrHandler) as server:
        server.serve_forever()

