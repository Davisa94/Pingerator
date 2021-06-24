import datetime as dt
import os
import pandas as pd
from pythonping import ping

# G lobal Values
_GOOGLEOUTFILE = "/responses/googleResponses - Copy.csv"
_CLOUDFLAREOUTFILE = "/responses/cloudFlareResponses - Copy.csv"
_OPENDNSOUTFILE = "/responses/openDns - Copy.csv"
_CLOUDFLAREHOST = "1.1.1.1"
_GOOGLEHOST = "8.8.8.8"
_OPENDNSHOST = "208.67.222.222"
_OUTAGESFILE = "/responses/outages.csv"
_ALLHOSTS = ["1.1.1.1", "8.8.8.8","208.67.222.222"]
runningDir = os.path.dirname(__file__)

class Outage:
    def __init__(self, occurrences, datetime, time_start, time_stop, hosts):
        self.occurrences = occurrences
        self.datetime = datetime
        self.time_start = time_start
        self.time_stop = time_stop
        self.hosts = hosts
    def __str__(self):
        return "Occurences: {}, Datetime: {}, Time Start: {}, Time stop {}, hosts {}".format(self.occurrences, self.datetime,self.time_start,self.time_stop,self.hosts)

    def reset(self):
        self.occurrences = 0
        self.datetime = dt.datetime(1996,10,10)
        self.time_start = dt.time()
        self.time_stop = dt.time()
        self.hosts = list()


# generates an object for storing the results of the pings and
# for use in writing to the csv file when given an response object
def generateInObject(file):
    fileResponse = pd.read_csv(file)
    print(fileResponse)
    return fileResponse

def countOutagesSimple(file_response, running_total=0):
    outages = file_response.loc[file_response["Responded?"] == False]
    print(outages)
    return outages

def printDataframeToFile(writableResponses, file):
    writableResponses.to_csv(file, header=None, mode="a")

def collate(fr_1, fr_2, fr_3):
    frames_to_merge = [fr_1, fr_2, fr_3]
    merged = pd.concat(frames_to_merge)
    merged["DateTime"] = merged["Date"].str.cat(merged["Time"],sep=" ")
    merged["DateTime"] = pd.to_datetime(merged["DateTime"])
    del merged["Date"]
    del merged["0"]
    merged = merged.sort_values(by="DateTime")
    print(merged)
    return merged

def countOutages(merged_df):
    results = []
    hosts = []
    prevRow = []
    outage = Outage(0,0,0,0,list())
    print(outage)
    outage.reset()

    for index, row in merged_df.iterrows():
        host = row["Host"]
        time = dt.time(row["DateTime"])
        date = row["DateTime"]
        diff = time - outage.time_stop
        print(diff)
        if diff < dt.timedelta(seconds=30):
            outage.datetime = date
            outage.occurrences += 1
            outage.time_stop = time
            outage.hosts.append(host)
            print(outage)

        else:
            if _ALLHOSTS in outage.hosts:
                results.append(outage)
            outage.reset()
            outage.time_start = time
            outage.occurrences += 1
            outage.datetime = time

    return results
def pinger(host):
    responses = ping(host, count=1)
    return responses




def main():
    #googleresults:
    fr_goog = generateInObject(runningDir + _GOOGLEOUTFILE)
    outages_google = countOutagesSimple(file_response=fr_goog)
    #running_total = outages_google.shape
    #cloudflare
    fr_cloud = generateInObject(runningDir + _CLOUDFLAREOUTFILE)
    outages_cloud = countOutagesSimple(fr_cloud)
    #running_total += len(outages_cloud.rows)
    #OpenDNS
    fr_open = generateInObject(runningDir + _OPENDNSOUTFILE)
    outages_open = countOutagesSimple(fr_open)
    #running_total += len(outages_open.rows)
    merged_outages = collate(outages_google,outages_cloud,outages_open)
    #outages = countOutages(merged_outages)
    printDataframeToFile(merged_outages, runningDir + _OUTAGESFILE)
    #print(outages)



if __name__ == '__main__':
    main()
