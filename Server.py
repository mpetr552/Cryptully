import socket
import Exceptions

from EncSocket   import EncSocket

class Server:

    def __init__(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Allow reuse of port
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except socket.error as se:
            raise Exceptions.NetworkError(str(se))


    def startServer(self, port):
        try:
            self.sock.bind(('localhost', port))
            self.sock.listen(5)
        except socket.error as se:
            raise Exceptions.NetworkError(str(se))


    def accept(self):
        (clientSock, clientAddr) = self.sock.accept()
        return EncSocket(clientAddr, clientSock)