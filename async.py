import asyncio


async def abra():
    print('alla')
    asyncio.sleep(10)
    return 'ello'


async def main():
    joke = await abra()
    print(joke+"==")
main()
