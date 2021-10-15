from multiprocessing.managers import BaseManager
from queue import Queue

from _base import m

server = m.get_server()
server.serve_forever()
