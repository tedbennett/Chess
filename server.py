# !/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from constant import PORT
import json


class Server:
    def __init__(self):
        self.clients = {}
        self.addresses = {}
        self.start_server()

    def start_server(self):
        SERVER.listen(5)
        print("Waiting for connection...")
        accept_thread = Thread(target=self.accept_incoming_connections)
        accept_thread.start()
        accept_thread.join()
        SERVER.close()

    def accept_incoming_connections(self):
        """Sets up handling for incoming clients."""
        num_clients = 0
        while True:
            client, client_address = SERVER.accept()
            self.addresses[client] = client_address
            print("Player {} has connected.".format(len(self.clients) + 1))
            Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        """Handles a single client connection."""
        name = str(len(self.clients) + 1)
        self.clients[client] = name
        join_message = json.dumps({"key": "JOIN", "payload": {}, "name": name})
        self.broadcast(join_message)

        while True:
            msg = client.recv(BUFSIZ)
            message = json.loads(msg.decode("utf-8"))
            if message["key"] != "EXIT":
                message["name"] = name
                self.broadcast(json.dumps(message))
            else:
                client.close()
                del self.clients[client]
                print("Player {} has disconnected.".format(self.clients[client]))
                exit_message = json.dumps({"key": "EXIT", "payload": {}, "name": name})
                self.broadcast(exit_message)
                del self.addresses[client]
                break

    def broadcast(self, msg):
        """Broadcasts a message to all the clients."""
        for sock in self.clients:
            sock.send(bytes(msg, "utf-8"))


if __name__ == "__main__":
    HOST = ''
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind(ADDR)

    server = Server()
