$computerName = "Mikael_Old"  # Set to the name for this computer
$outputFile = "computer_specs_$computerName.txt"

# Run all commands and append to file
Get-ComputerInfo > $outputFile
Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors >> $outputFile
Get-CimInstance Win32_PhysicalMemory | Select-Object Capacity, Speed, Manufacturer >> $outputFile
Get-CimInstance Win32_LogicalDisk | Select-Object Caption, Size, FreeSpace, FileSystem >> $outputFile
Get-CimInstance Win32_VideoController | Select-Object Name, DriverVersion, AdapterRAM >> $outputFile
Get-NetAdapter | Select-Object Name, Status, MacAddress >> $outputFile
Get-NetIPAddress | Select-Object InterfaceAlias, IPAddress >> $outputFile
Get-CimInstance Win32_Product | Select-Object Name, Version >> $outputFile
Get-CimInstance Win32_Battery | Select-Object EstimatedChargeRemaining, BatteryStatus >> $outputFile
Get-Counter '\Processor(_Total)\% Processor Time' -SampleInterval 1 -MaxSamples 1 >> $outputFile
Get-CimInstance Win32_OperatingSystem | Select-Object LastBootUpTime, TotalVisibleMemorySize, FreePhysicalMemory >> $outputFile

Write-Host "Specs collected in $outputFile"