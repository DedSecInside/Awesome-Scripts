@ECHO OFF
::### Set Proxy
:: Please define your proxy where <PROXY IP> is located below
:: If local exclusions are needed, add them to <EXC> seperated by ";"

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /V AutoDetect /T REG_DWORD /D 0 /F
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /V ProxyEnable /T REG_DWORD /D 1 /F
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /V ProxyServer /T REG_SZ /D "<PROXY IP>" /F
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /V ProxyOverride /T REG_SZ /D "<EXC>;<local>" /F

:: Created by Rob Fitz

