import asyncio
################################################################################
async def handle_connection(reader, writer):
    content = b'<html>'\
              b'<head>'\
              b'<title>Title</title>'\
              b'</head>'\
              b'<body>'\
              b'Hello World'\
              b'</body>'\
              b'</html>'
    writer.write(b'HTTP/1.0 200 OK\r\n')
    writer.write('Content-Length: {}\r\n'.format(len(content)).encode('utf-8'))
    writer.write(b'Content-Type: text/html\r\n')
    writer.write(b'\r\n')
    writer.write(content)
    await writer.drain()
    writer.close()
################################################################################
async def main():
    async with (
        await asyncio.start_server(
            handle_connection,
            port = 8888
        )
    ) as server:
        await server.serve_forever()
################################################################################
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('User stopped server')
