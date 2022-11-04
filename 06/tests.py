# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=protected-access


import io
import sys
import threading
import unittest.mock
from unittest.mock import Mock

from client.client import Client
from server.server import Server


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.func_output = io.StringIO()
        sys.stdout = self.func_output

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__


class TestClient(BaseTest):
    @unittest.mock.patch("socket.socket")
    def test_send_urls(self, sock):
        sock.return_value.__enter__.return_value = sock.return_value
        sock.return_value.recv.return_value = b"123"
        client = Client("./client/urls.txt", 1)
        client._send_urls(client.urls[0:1])
        sys.stdout = sys.__stdout__

        self.assertEqual(self.func_output.getvalue(), "123\n")


class TestServer(BaseTest):
    def test_handle_url(self):
        c_mocked = Mock()
        server = Server(1, 1, port=9999)
        server._handle_url("https://mail.ru/", c_mocked)
        server._close()

        self.assertEqual(server.processed, 1)


class TestIntegration(BaseTest):
    def test_integration(self):
        threads = {}

        client = Client("./client/urls.txt", 3, port=9998)
        server = Server(4, 2, port=9998)

        threads["server"] = threading.Thread(
            name="server",
            target=server.start,
        )

        threads["client"] = threading.Thread(
            name="client",
            target=client.send_urls,
        )

        try:
            threads["server"].start()
            threads["client"].start()

            threads["client"].join()
            threads["server"].join()
        except KeyboardInterrupt:
            server._close()

        self.assertEqual(server.processed, 100)
        self.assertIn("Урлов обработано: 100", self.func_output.getvalue())
