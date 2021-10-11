import asyncio
import time
################################################################################
async def main():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888
    )
    while not reader.at_eof():
        data = await reader.readline()
        print('[{}] Received: {}'.format(time.strftime('%X'), data))
################################################################################
if __name__ == '__main__':
    asyncio.run(main())
