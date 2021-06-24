import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '10', host]

    return subprocess.run(command) == 0

def ping2(host):
    return subprocess.run("ping 8.8.8.8 -t >> D:\\Users\\skyac\\PycharmProjects\\pingerator\\src\\responses.csv", capture_output=True) == 0
def main():
    sp = ping2("8.8.8.8")
    print(sp.communicate)


if __name__ == "__main__":
    main()
