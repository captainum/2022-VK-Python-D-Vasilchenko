# pylint: disable=missing-module-docstring


import argparse
import sys

from .server import Server

parser = argparse.ArgumentParser()

parser.add_argument(
    "-w",
    type=int,
)
parser.add_argument(
    "-k",
    type=int,
)

args = parser.parse_args(sys.argv[1:])

server = Server(args.w, args.k)
server.start()
