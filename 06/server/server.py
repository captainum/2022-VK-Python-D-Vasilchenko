# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=unspecified-encoding
# pylint: disable=too-few-public-methods
# pylint: disable=missing-timeout


import json
import socket
import threading
from collections import Counter
from uuid import uuid4

import lxml.html
import requests


class Server:
    def __init__(self, workers: int, k: int, host="localhost", port=9997):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.workers = workers
        self.k = k

        self.processed = 0
        self.threads = {}
        self.mutex = threading.Lock()

    def start(self):
        self.s.listen()
        try:
            while True:
                c, _ = self.s.accept()
                url = c.recv(1024).strip()
                while len(self.threads) == self.workers:
                    for n, t in self.threads.copy().items():
                        if not t.is_alive():
                            self.threads.pop(n)

                thread_name = f"thread_{uuid4().urn.split(':')[2]}"
                self.threads[thread_name] = threading.Thread(
                    name=thread_name,
                    target=self._handle_url,
                    args=(url, c),
                )
                self.threads[thread_name].start()
        except (KeyboardInterrupt, ConnectionAbortedError):
            self.s.close()

    def _close(self):
        self.s.close()

    def _handle_url(self, url, c):
        resp = requests.get(url)
        html = lxml.html.fromstring(resp.text)
        tags = Counter([tag.tag for tag in html.iter()])

        tags = sorted(
            filter(lambda data: isinstance(data[0], str), tags.items()),
            key=lambda data: data[1],
            reverse=True,
        )

        to_send = dict(tags[:self.k])

        c.send(json.dumps(to_send).encode("utf-8"))
        c.close()

        with self.mutex:
            self.processed += 1
            print("Урлов обработано:", self.processed, flush=True)
