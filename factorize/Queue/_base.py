from multiprocessing.managers import BaseManager
from queue import Queue


class QueueManager(BaseManager):
    pass


queue = Queue()

QueueManager.register('get_queue', callable=lambda: queue)

m = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
