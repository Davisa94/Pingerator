Write-Output "This acript creates 3 jobs that track interneet connectivity, the log file is stored in the C drive Base Directory" 
Start-Job -FilePath .\pingerator.ps1 -ArgumentList 8.8.8.8 -Name GoogleDNSPing
Start-Job -FilePath .\pingerator.ps1 -ArgumentList 1.1.1.1 -Name CloudFlareDNSPing
Start-Job -FilePath .\pingerator.ps1 -ArgumentList 208.67.222.222 -Name OpenDNSPing
