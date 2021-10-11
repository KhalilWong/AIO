import asyncio
################################################################################
async def main():
    p = await asyncio.create_subprocess_shell('dir')
    await p.wait()
################################################################################
if __name__ == '__main__':
    asyncio.run(main())
