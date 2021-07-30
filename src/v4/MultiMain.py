import time
import os
import speedtest
from modules import PingTest
from modules import GlobalValues as GV
from modules import FileManager as FM
##########################################################################
# This is v4 of the ISP accountability suite which adds a speed test and
# splits the project into a variety of files for portability.
# Author: Austin Benitez
# Internal Project Name: Pingerator
##########################################################################

# Global Values
runningDir = os.path.dirname(__file__)
class SpeedyTester:
    def __init__(self, desktop):
        self.file = desktop + GV._SPEEDSOUTFILE
        FM.generateFile(self.file, GV._SPEEDDICT)


    def upload_test(self):
        pass
    def run(self):
        print("The full path to my log files is at: {} ".format(self.file))
        st = speedtest.Speedtest()
        # print("Success" if res.success else " Failed")
        print("Speeds: ", st)
        wr = FM.generateOutSpeedObject(st)
        FM.printDataframeToFile(wr, self.file)\



class DataAnalyzer:
    def __init__(self):
        pass

    def analyze(self):
        place_holder_message = "Analyzing the data. Press any key to exit the application."
        print(place_holder_message)

def main():
    desktop_dir = FM.generateDesktopPath()
    home_dir = FM.generateHomeFolder(desktop_dir)
    #check if files exit, if they do  move along, if not, generate them with appropriate headers

    print("The detected desktop directory is {} and will be used for storing the data folder".format(home_dir))
    pingG = PingTest.PingGoogle(home_dir)
    pingC = PingTest.PingCloudFlare(home_dir)
    pingO = PingTest.PingOpenDNS(home_dir)
    analyzer = DataAnalyzer()
    st = SpeedyTester(home_dir)

    while True:
        time.sleep(8)
        pingG.run()
        pingC.run()
        pingO.run()
        st.run()

    input("Press Enter To Continue")
    exit()


if __name__ == '__main__':
    main()
