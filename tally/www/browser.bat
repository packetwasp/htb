
del C:\Users\Sarah\Desktop\session_id.txt

REM output current session information to file
qwinsta | findstr ">" > C:\Users\Sarah\Desktop\session_id.txt

REM query file for session id
FOR /F "tokens=3" %%a IN (C:\Users\Sarah\Desktop\session_id.txt) DO SET sessionid=%%a

del C:\Users\Sarah\Desktop\session_id.txt

REM only if console user, enter loop
if %sessionid% EQU 1 goto LOOP
if %sessionid% GTR 1 goto EXIT

:LOOP

REM kill any open instances of firefox and crashreporter
taskkill /F /IM firefox.exe > nul 2>&1
taskkill /F /IM crashreporter.exe > nul 2>&1

REM copy latest mockups to webroot
copy /Y C:\FTP\Intranet\index.html C:\inetpub\wwwroot\HRTJYKYRBSHYJ\index.html

REM browse file
start "" "C:\Program Files (x86)\Mozilla Firefox\Firefox.exe" "http://127.0.0.1:81/HRTJYKYRBSHYJ/index.html"

REM wait
ping 127.0.0.1 -n 800 > nul

if not ErrorLevel 1 goto :LOOP

:EXIT
exit
