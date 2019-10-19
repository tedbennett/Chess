import pickle
import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1241))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established.")

    move = {"Piece": "Rook", "Colour": "White", "x": 5, "y": 2}
    message = pickle.dumps(move)
    message = bytes(f"{len(message):<{HEADERSIZE}}", 'utf-8') + message
    client_socket.send(message)
