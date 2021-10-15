from _base import m

m.connect()
queue = m.get_queue()
value = "Hello Dima!"
print(f'Send to server - {value}')
queue.put(value)
