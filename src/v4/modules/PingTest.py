
_DIRECTORYMAIN = '\\InternetTester\\responses'
_GOOGLEOUTFILE = '\\googleResponses.csv'
_CLOUDFLAREOUTFILE = "\\cloudFlareResponses.csv"
_OPENDNSOUTFILE = "\\openDns.csv"
_SPEEDSOUTFILE = "\\speeds.csv"
_CLOUDFLAREHOST = "1.1.1.1"
_GOOGLEHOST = "8.8.8.8"
_OPENDNSHOST = "208.67.222.222"
_PINGDICT = {
    'Day': ['Day'],
    'TimeStamp': ['TimeStamp'],
    'Host': ['Host'],
    'responseTIme': ['ResponseTime'],
    'Succeeded': ['Succeeded']
}
_SPEEDDICT = {
    'Day': ['Day'],
    'TimeStamp': ['TimeStamp'],
    'UploadSpeed': ['UploadSpeed'],
    'DownloadSpeed': ['DownloadSpeed'],
    'FullResponse': ['FullResponse']
}
runningDir = os.path.dirname(__file__)

class Pinger:
    def pinger(host):
        responses = ping(host, count=1)
        return responses


class PingGoogle(Pinger):
    def __init__(self, desktop):
        self.host = _GOOGLEHOST
        self.file = desktop + _GOOGLEOUTFILE
        generateFile(self.file, _PINGDICT)


    def run(self):
        print("The full path to my log files is at: {} ".format(self.file))
        responses = pinger(self.host)
        res = {}
        for response in responses:
            res = response
        # print("Success" if res.success else " Failed")
        print(res)
        wr = generateOutObject(res, self.host)
        printDataframeToFile(wr, self.file)


class PingOpenDNS(Pinger):
    def __init__(self, desktop):
        self.host = _OPENDNSHOST
        self.file = desktop + _OPENDNSOUTFILE
        generateFile(self.file, _PINGDICT)

    def run(self):
        responses = pinger(self.host)
        res = {}
        for response in responses:
            res = response
        # print("Success" if res.success else " Failed")
        print(res)
        wr = generateOutObject(res, self.host)
        printDataframeToFile(wr, self.file)


class PingCloudFlare(Pinger):
    def __init__(self, desktop):
        self.host = _CLOUDFLAREHOST
        self.file = desktop + _CLOUDFLAREOUTFILE
        generateFile(self.file, _PINGDICT)

    def run(self):
        responses = pinger(self.host)
        res = {}
        for response in responses:
            res = response
        # print("Success" if res.success else " Failed")
        print(res)
        wr = generateOutObject(res, self.host)
        printDataframeToFile(wr, self.file)
