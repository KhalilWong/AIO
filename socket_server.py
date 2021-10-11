import asyncio
################################################################################
async def handle_echo(reader, writer):
    for i in range(1, 6):
        writer.write('Count {}\n'.format(i).encode('utf-8'))
        await writer.drain()
        await asyncio.sleep(1)
    writer.close()
################################################################################
async def main():
    port = 8888
    server = await asyncio.start_server(
        handle_echo,
        port = port
    )
    print('Serving on port {}'.format(port))
    async with server:
        await server.serve_forever()
################################################################################
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('User stopped server')
