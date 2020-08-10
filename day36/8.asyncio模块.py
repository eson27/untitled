import asyncio # 这个原生模块 使用麻烦 了解即可，实用第三方封装好的模块
async def func(name):
    print('start',name)
    #await 可能会发生阻塞的方法
    #await关键字必须写在一个async函数里
    await asyncio.sleep(1)
    print('end')

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([func('test'),func('haha')]))
