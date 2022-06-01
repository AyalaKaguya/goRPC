from ayn import BaseRPCClient

c = BaseRPCClient()
c.connect('127.0.0.1', 2550)
while True:
    res = c.add(1, 2, c=3)
    print(f'res1: {res}')
    res = c.funcall('add',1,2,c=3)
    print(f'res2: {res}')
    res = c.raw_funcall('add',1,2,c=3)
    print(f'res3: {res}')
c.close()