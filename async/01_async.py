import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")  

def another_task():
    print("This is another task.")

if __name__ == "__main__":
    asyncio.run(main())
    another_task()