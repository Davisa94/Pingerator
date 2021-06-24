import time
import os
import pandas as pd
from pythonping import ping

# G lobal Values
_GOOGLEOUTFILE = "/responses/googleResponses.csv"
_CLOUDFLAREOUTFILE = "/responses/cloudFlareResponses.csv"
_OPENDNSOUTFILE = "/responses/openDns.csv"
_CLOUDFLAREHOST = "1.1.1.1"
_GOOGLEHOST = "8.8.8.8"
_OPENDNSHOST = "208.67.222.222"
runningDir = os.path.dirname(__file__)


# generates an object for storing the results of the pings and
# for use in writing to the csv file when given an response object
def generateOutObject(response, host):
    # get current time
    succeeded = response.success
    currDate = pd.datetime.now().date()
    currTime = pd.datetime.now().time()
    dict = {
        "Day": [currDate],
        'TimeStamp': [currTime],
        'Host': [host],
        "responseTIme": [response],
        "Succeeded": [succeeded]
    }
    writableResponse = pd.DataFrame.from_dict(dict)
    return writableResponse


def printDataframeToFile(writableResponses, file):
    writableResponses.to_csv(file, header=None, mode="a")


def pinger(host):
    responses = ping(host, count=1)
    return responses


class PingGoogle:
    def __init__(self):
        self.host = _GOOGLEHOST
        self.file = runningDir + _GOOGLEOUTFILE

    def run(self):
        responses = pinger(self.host)
        res = {}
        for response in responses:
            res = response
        # print("Success" if res.success else " Failed")
        print(res)
        wr = generateOutObject(res, self.host)
        printDataframeToFile(wr, self.file)


class PingOpenDNS:
    def __init__(self):
        self.host = _OPENDNSHOST
        self.file = runningDir + _OPENDNSOUTFILE

    def run(self):
        responses = pinger(self.host)
        res = {}
        for response in responses:
            res = response
        # print("Success" if res.success else " Failed")
        print(res)
        wr = generateOutObject(res, self.host)
        printDataframeToFile(wr, self.file)


class PingCloudFlare:
    def __init__(self):
        self.host = _CLOUDFLAREHOST
        self.file = runningDir + _CLOUDFLAREOUTFILE

    def run(self):
        responses = pinger(self.host)
        res = {}
        for response in responses:
            res = response
        # print("Success" if res.success else " Failed")
        print(res)
        wr = generateOutObject(res, self.host)
        printDataframeToFile(wr, self.file)


def main():
    pingG = PingGoogle()
    pingC = PingCloudFlare()
    pingO = PingOpenDNS()

    while True:
        time.sleep(8)
        pingG.run()
        pingC.run()
        pingO.run()


if __name__ == '__main__':
    main()
