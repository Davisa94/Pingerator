$_OUTPUTFILE = "D:\Users\skyac\PycharmProjects\pingerator\src\responses.csv"
while (1 -eq 1) {
    echo "Getting Date"
    Get-Date >> $_OUTPUTFILE
    try {
        Echo "Testing Connection"
        Test-Connection 8.8.8.8 -Count 1 >> $_OUTPUTFILE
    }
    catch [TestConnectionException] {
        Echo "timed out connection"
        Add-Content -Path $_OUTPUTFILE -Value "Connection Timed Out"
    }
    catch [ResourceUnavailable]
    {
        Echo "timed out connection"
        Add-Content -Path $_OUTPUTFILE -Value "Connection Timed Out"
    }
    
}
