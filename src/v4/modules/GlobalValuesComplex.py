
class GlobalValues:
    def __init__(self):
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

    @property
    def DIRECTORYMAIN(self):
        return self._DIRECTORYMAIN

    @property
    def GOOGLEOUTFILE(self):
        return self._GOOGLEOUTFILE

    @property
    def CLOUDFLAREOUTFILE(self):
        return self._CLOUDFLAREOUTFILE
    
    @property
    def OPENDNSOUTFILE(self):
        return self._OPENDNSFILE
    
    @property
    def SPEEDSOUTFILE(self):
        return self.__SPEEDSOUTFILE

    @property
    def CLOUDFLAREHOST(self):
        return self._CLOUDFLAREHOST

    @property
    def GOOGLEHOST(self):
        return self._GOOGLEHOST

    @property
    def OPENDNSHOST(self):
        return self._OPENDNSHOST

    @property
    def PINGDICT(self):
        return self._PINGDICT

    @property
    def SPEEDDICT(self):
        return self._SPEEDDICT