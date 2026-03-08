To standardize the comparison between your computers (including your second one as Terese), you should run the same set of terminal commands on each computer to collect consistent hardware, software, and system information. This ensures the data is comparable across all machines. Since you're on Windows (PowerShell), I'll provide commands that work in PowerShell (run them in an elevated/admin PowerShell session for full access).

### Key Assumptions and Setup
- **Computers involved**: Based on the files in computer, it looks like there are 3 computers (Mikael's old one, your DELL, and Mikael's new one). Run these on all 3, including your second computer.
- **Output standardization**: For each computer, run the commands and redirect the output to a text file (e.g., `computer_specs_<name>.txt`). This way, you can easily compare the files later (e.g., using `fc` as I suggested before).
- **Why these commands?**: They cover essential specs like OS, CPU, RAM, storage, GPU, network, and performance metrics. They're non-destructive and safe to run.
- **How to run**: Open PowerShell as admin on each computer, navigate to a folder (e.g., `cd D:\udemy\llm_eng\w-terese\computer`), and run the commands one by one or as a batch script (see below).
- **Batch script option**: To automate, create a `.ps1` script on each computer with the commands below, then run it. This saves time and ensures consistency.

### Full List of Terminal Commands
Run these in sequence on each computer. Replace `<computer_name>` with something like `Terese_DELL`, `Terese_Second`, `Mikael_Old`, etc., for the output file.

1. **Get OS and system info** (basic overview):
   ```
   systeminfo > "computer_specs_<computer_name>.txt"
   ```

2. **Get CPU details**:
   ```
   wmic cpu get name, numberofcores, numberoflogicalprocessors >> "computer_specs_<computer_name>.txt"
   ```

3. **Get RAM/memory details** (total and slots):
   ```
   wmic memorychip get capacity, speed, manufacturer >> "computer_specs_<computer_name>.txt"
   ```

4. **Get storage/disk details** (drives and space):
   ```
   wmic logicaldisk get caption, size, freespace, filesystem >> "computer_specs_<computer_name>.txt"
   ```

5. **Get GPU/graphics details**:
   ```
   wmic path win32_videocontroller get name, driverversion, adapterram >> "computer_specs_<computer_name>.txt"
   ```

6. **Get network adapters and IP config**:
   ```
   ipconfig /all >> "computer_specs_<computer_name>.txt"
   ```

7. **Get installed software/programs** (top-level list; may take time):
   ```
   wmic product get name, version >> "computer_specs_<computer_name>.txt"
   ```

8. **Get battery info** (if laptop; skip for desktops):
   ```
   wmic path win32_battery get estimatedchargeremaining, batterystatus >> "computer_specs_<computer_name>.txt"
   ```

9. **Get performance metrics** (CPU usage snapshot):
   ```
   Get-Counter '\Processor(_Total)\% Processor Time' -SampleInterval 1 -MaxSamples 1 >> "computer_specs_<computer_name>.txt"
   ```

10. **Get uptime and boot time**:
    ```
    wmic os get lastbootuptime, totalvisiblememorysize, freephysicalmemory >> "computer_specs_<computer_name>.txt"
    ```

### Automation Script (Optional but Recommended)
To run all commands at once without manual redirection each time, create a PowerShell script file (e.g., `get_specs.ps1`) on each computer with this content:

```powershell
$computerName = "<computer_name>"  # Replace with the name for this computer
$outputFile = "computer_specs_$computerName.txt"

# Run all commands and append to file
systeminfo > $outputFile
wmic cpu get name, numberofcores, numberoflogicalprocessors >> $outputFile
wmic memorychip get capacity, speed, manufacturer >> $outputFile
wmic logicaldisk get caption, size, freespace, filesystem >> $outputFile
wmic path win32_videocontroller get name, driverversion, adapterram >> $outputFile
ipconfig /all >> $outputFile
wmic product get name, version >> $outputFile
wmic path win32_battery get estimatedchargeremaining, batterystatus >> $outputFile
Get-Counter '\Processor(_Total)\% Processor Time' -SampleInterval 1 -MaxSamples 1 >> $outputFile
wmic os get lastbootuptime, totalvisiblememorysize, freephysicalmemory >> $outputFile

Write-Host "Specs collected in $outputFile"
```

- Save this as `get_specs.ps1` in the same folder on each computer.
- Run it with: `.\get_specs.ps1` (as admin).
- Copy the resulting `.txt` files to computer for comparison.

### Next Steps for Comparison
- After collecting the files, use the `fc` commands I provided earlier to diff them.
- If you need more advanced analysis (e.g., parsing the output), you could import the `.txt` files into Excel or a tool like Beyond Compare for side-by-side views.
- If any command fails (e.g., due to permissions), run PowerShell as admin.

If you need commands for a different OS (e.g., if one computer is Linux/Mac), or more specific metrics, let me know!