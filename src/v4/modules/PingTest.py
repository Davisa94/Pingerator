from modules import GlobalValues as GV
from modules import FileManager as FM
from pythonping import ping

class Pinger:
    def pinger(self, host):
        responses = ping(host, count=1)
        return responses


class PingGoogle(Pinger):
    def __init__(self, desktop):
        self.host = GV._GOOGLEHOST
        self.file = desktop + GV._GOOGLEOUTFILE
        FM.generateFile(self.file, GV._PINGDICT)


    def run(self):
        print("The full path to my log files is at: {} ".format(self.file))
        responses = self.pinger(self.host)
        res = {}
        for response in responses:
            res = response
        # print("Success" if res.success else " Failed")
        print(res)
        wr = FM.generateOutObject(res, self.host)
        FM.printDataframeToFile(wr, self.file)


class PingOpenDNS(Pinger):
    def __init__(self, desktop):
        self.host = GV._OPENDNSHOST
        self.file = desktop + GV._OPENDNSOUTFILE
        FM.generateFile(self.file, GV._PINGDICT)

    def run(self):
        responses = self.pinger(self.host)
        res = {}
        for response in responses:
            res = response
        # print("Success" if res.success else " Failed")
        print(res)
        wr = FM.generateOutObject(res, self.host)
        FM.printDataframeToFile(wr, self.file)


class PingCloudFlare(Pinger):
    def __init__(self, desktop):
        self.host = GV._CLOUDFLAREHOST
        self.file = desktop + GV._CLOUDFLAREOUTFILE
        FM.generateFile(self.file, GV._PINGDICT)

    def run(self):
        responses = self.pinger(self.host)
        res = {}
        for response in responses:
            res = response
        # print("Success" if res.success else " Failed")
        print(res)
        wr = FM.generateOutObject(res, self.host)
        FM.printDataframeToFile(wr, self.file)
