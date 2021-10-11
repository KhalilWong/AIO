import asyncio
################################################################################
async def main():
    reader, writer = await asyncio.open_connection(
        'yunp.top', '80'
    )
    writer.write(b'GET / HTTP/1.1\r\n')
    writer.write(b'Host: yunp.top\r\n')
    writer.write(b'Connection: close\r\n')
    writer.write(b'\r\n')
    await writer.drain()
    result = await reader.read()
    print(result.decode('utf-8'))
################################################################################
if __name__ == '__main__':
    asyncio.run(main())
