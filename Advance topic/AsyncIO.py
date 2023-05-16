## DEMO CODE

# import asyncio
#
#
# async def function1():
#     await asyncio.sleep(1)
#     print("func 1")
#     return "Sambit"
#
#
# async def function2():
#     await asyncio.sleep(1)
#     print("func 2")
#
#
# async def function3():
#     await asyncio.sleep(4)
#     print("func 3")
#
#
# async def main():
#     # task = asyncio.create_task(function1())  # Jab bhi usko time milega, tab chalega, it doesnot maintain syncronization
#     # # await function1()
#     # await function2()
#     # await function3()
#
#     L = await asyncio.gather(  # it will drive all the vale in one time
#         function1(),
#         function2(),
#         function3()
#     )
#     print(L)
#
#
# asyncio.run(main())


## Practical Example

import asyncio
import requests


async def function1():
    print("func1")
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("photo/instagram.ico", "wb").write(response.content)


async def function2():
    print("func 2")
    URL = "https://facebook.com/favicon.ico"
    response = requests.get(URL)
    open("photo/facebook.ico", "wb").write(response.content)


async def function3():
    print("func 3")
    URL = "https://siligurisutra.com/favicon.ico"
    response = requests.get(URL)
    open("photo/siligurisutra.ico", "wb").write(response.content)


async def main():
    # task = asyncio.create_task(function1())  # Jab bhi usko time milega, tab chalega, it doesnot maintain syncronization
    # # await function1()
    # await function2()
    # await function3()

    L = await asyncio.gather(  # it will drive all the vale in one time
        function1(),
        function2(),
        function3()
    )
    print(L)


asyncio.run(main())


