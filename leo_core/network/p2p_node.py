import socket
import threading
import json
import time
from typing import List, Callable

class P2PNode:
    """
    Project LEO: Decentralized Networking Layer.
    Handles peer discovery and message broadcasting for ADMM consensus.
    """
    def __init__(self, host: str = '127.0.0.1', port: int = 5000):
        self.host = host
        self.port = port
        self.peers: List[tuple] = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.on_message_received: Callable = None
        self.running = True

    def start(self):
        """Starts the node's server to listen for incoming peer connections."""
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"[P2P] Node started on {self.host}:{self.port}")
        
        thread = threading.Thread(target=self._listen)
        thread.daemon = True
        thread.start()

    def _listen(self):
        while self.running:
            try:
                client, address = self.server_socket.accept()
                threading.Thread(target=self._handle_client, args=(client, address)).start()
            except Exception as e:
                if self.running:
                    print(f"[P2P] Listen error: {e}")

    def _handle_client(self, client, address):
        try:
            data = client.recv(4096).decode('utf-8')
            if data:
                message = json.loads(data)
                if self.on_message_received:
                    self.on_message_received(message, address)
        except Exception as e:
            print(f"[P2P] Error handling client {address}: {e}")
        finally:
            client.close()

    def connect_to_peer(self, host: str, port: int):
        """Adds a peer to the node's list of active connections."""
        if (host, port) not in self.peers and (host != self.host or port != self.port):
            self.peers.append((host, port))
            print(f"[P2P] Connected to peer {host}:{port}")

    def broadcast(self, message: dict):
        """Sends a message to all connected peers."""
        for peer_host, peer_port in self.peers:
            self.send_to_peer(peer_host, peer_port, message)

    def send_to_peer(self, host: str, port: int, message: dict):
        """Sends a direct message to a specific peer."""
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((host, port))
            client.send(json.dumps(message).encode('utf-8'))
            client.close()
        except Exception as e:
            print(f"[P2P] Failed to send message to {host}:{port}: {e}")

    def stop(self):
        self.running = False
        self.server_socket.close()
