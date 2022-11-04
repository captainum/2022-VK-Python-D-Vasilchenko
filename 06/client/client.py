# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name
# pylint: disable=unspecified-encoding
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods


import socket
import threading


class Client:
    def __init__(self, path: str, m: int, host="localhost", port=9997):
        self.host = host
        self.port = port
        with open(path, "r") as f:
            self.urls = list(map(str.strip, f.readlines()))
        self.m = m

    def _send_urls(self, urls):
        for url in urls:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                sock.sendall(bytes(url, "utf-8"))
                received = str(sock.recv(1024), "utf-8")
                print(received)

    def send_urls(self):
        urls_size = len(self.urls)

        threads = [
            threading.Thread(
                target=self._send_urls,
                args=(
                    self.urls[
                        i * urls_size // self.m: (i + 1) * urls_size // self.m
                    ],
                ),
            )
            for i in range(self.m)
        ]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
