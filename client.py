import pickle
import socket

# HEADERSIZE = 10
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 1241))
#
# while True:
#     move = b''
#     new_message = True
#     while True:
#         message = s.recv(16)
#         if new_message:
#             message_length = int(message[:HEADERSIZE])
#             new_message = False
#
#         move += message
#
#         if len(move) - HEADERSIZE == message_length:
#             print("Full message received")
#             print(pickle.loads(move[HEADERSIZE:]))
#             new_msg = True
import time


class Client:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5555
        self.address = (self.host, self.port)

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(4096 * 8)

    def disconnect(self):
        self.client.close()

    def send(self, data):
        start_time = time.time()
        while time.time() - start_time < 5:
            try:
                self.client.send(pickle.dumps(data))
                reply = self.client.recv(4096 * 8)
                try:
                    reply = pickle.loads(reply)
                    break
                except Exception as e:
                    print(e)

            except socket.error as e:
                print(e)

        return reply
