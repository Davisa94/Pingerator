[CmdletBinding()]
Param (
    [String[]]$Destination = "8.8.8.8",
    [int32]$Count = 5,
    #in milliseconds
    [int32]$Interval = 1000,
    
    [Parameter(ValueFromPipeline=$true)]
    
    
    
    [string]$LogPath = "D:\Users\skyac\PycharmProjects\pingerator\src\responses4.csv"
)

$Ping = @()
#Test if path exists, if not, create it
If (-not (Test-Path (Split-Path $LogPath) -PathType Container))
{   Write-Verbose "Folder does not exist $(Split-Path $LogPath), creating..."
    New-Item (Split-Path $LogPath) -ItemType Directory | Out-Null
}

#Test if log file exists, if not seed it with a header row
If (-not (Test-Path $LogPath))
{   Write-Verbose "Log file doesn't exist: $($LogPath), creating..."
    Add-Content -Value '"TimeStamp","Source","Destination","IPV4Address","Status","ResponseTime"' -Path $LogPath
}

#Log collection loop
Write-Verbose "Beginning Ping monitoring of $Destination for $Count tries:"
While (1 -eq 1)
{   $Ping = Get-WmiObject Win32_PingStatus -Filter "Address = '$Destination'" | Select @{Label="TimeStamp";Expression={Get-Date}},@{Label="Source";Expression={ $_.__Server }},@{Label="Destination";Expression={ $_.Address }},IPv4Address,@{Label="Status";Expression={ If ($_.StatusCode -ne 0) {"Failed"} Else {"Succeeded"}}},ResponseTime
    $Result = $Ping | Select TimeStamp,Source,Destination,IPv4Address,Status,ResponseTime | ConvertTo-Csv -NoTypeInformation
    $Result[1] | Add-Content -Path $LogPath
    Write-verbose ($Ping | Select TimeStamp,Source,Destination,IPv4Address,Status,ResponseTime | Format-Table -AutoSize | Out-String)
    Write-Output $Ping
    Start-Sleep -Milliseconds $Interval
}