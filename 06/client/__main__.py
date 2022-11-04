# pylint: disable=missing-module-docstring


import argparse
import sys

from .client import Client

parser = argparse.ArgumentParser()

parser.add_argument(
    "-M",
    type=int,
)
parser.add_argument(
    "--file",
    type=str,
)

args = parser.parse_args(sys.argv[1:])

client = Client(args.file, args.M)
client.send_urls()
