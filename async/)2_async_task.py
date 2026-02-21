import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def another_task():
    print("This is another task.")

async def runner():
    await asyncio.gather(main(), another_task())

asyncio.run(runner())