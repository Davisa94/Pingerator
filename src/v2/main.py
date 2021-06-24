from pythonping import ping
import sys
import aiofiles as aiof
import asyncio
#Vars
global _GOOGLEIP, _SIZE, _PAYLOAD, _TIMEOUT, _original_Stdout
_GOOGLEIP = "8.8.8.8"
_SIZE = 32
_PAYLOAD = 32
_TIMEOUT = 4000
_original_Stdout = sys.stdout
_OUTPUT_FILE = "responses.csv"

def pingv2(address, fileStream):
    with open('responses.csv', 'a') as f:
        sys.stdout = f
    return ping(address, timeout=_TIMEOUT, size=_SIZE, verbose=True, count=10, out=f)

def init():
    with open('responses.csv', 'a') as f:
        sys.stdout = f
        return f

async def StoreResults():
    async with aiof.open(_OUTPUT_FILE, "w") as out:
        await out.write("hello world")
        await out.flush()
    print("done")

def printResults(response):
    for x in response:
        print(x)

def main():
    fileStream = init()
    pingv2(_GOOGLEIP, fileStream)




if __name__ == "__main__":
    main()