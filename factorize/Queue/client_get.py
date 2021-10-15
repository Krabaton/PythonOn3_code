from _base import m

m.connect()
queue = m.get_queue()
print('Wait data')
value = queue.get()

print(f'Get from server - {value}')
