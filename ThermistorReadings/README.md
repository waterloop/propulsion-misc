#### How log thermistor data
1. Upload ThermistorCode.ino to the arduino of your choice
2. Open puTTY.exe 
3. In Session --> select 'connection type' "Serial"
    3a. Rename 'Serial Line' field to "COM3" (default port)
    3b. 'Speed' should be set to "9600"
4. In Session>Logging --> select 'Session logging' "All session output"
    4a. Rename 'Log file name' to "{insert name here}.csv" -- only ".csv" is necessary
5. On bottom right, click the 'open' button and logging will begin immediately
6. To stop logging, close the terminal window 
7. Clean up the log by truncating the first and last row of the new .csv file
    7a. First row should be "Therm1,Therm2,Therm3,Therm4,..."

Additional resources can be found on [Google Drive](https://drive.google.com/drive/folders/1YmJ3xWW2S37qAnZtqaWsI0HqgEOOfY0c?usp=share_link)
(https://github.com/waterloop/propulsion-misc/ThermistorReadings/ThermistorWiring.PNG?raw=true)