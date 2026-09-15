import asyncio
async def Square(l):
    for i in l:
        await asyncio.sleep(0.4)
        print(f"the square iss {i*i}")
async def cube(l):
    for i in l:
        await asyncio.sleep(0.4)
        print(f"the cube is {i*i*i}")

    


async def main():
    l=[10,20,30] 
    await asyncio.gather(Square(l),cube(l))
asyncio.run(main())