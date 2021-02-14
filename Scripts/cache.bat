del /q "C:\Users\fiedo\AppData\Local\Temp\*"
del /q "C:\Windows\Temp\*"
del /q "C:\Windows\Prefetch\*"
del /q "C:\Windows\SoftwareDistribution\Download\*"

FOR /D %%p IN ("%userprofile%\AppData\Local\Temp\*.*") DO rmdir "%%p" /s /q
FOR /D %%p IN ("C:\Windows\Temp\*.*") DO rmdir "%%p" /s /q
FOR /D %%p IN ("C:\Windows\Prefetch\*.*") DO rmdir "%%p" /s /q
FOR /D %%p IN ("C:\Windows\SoftwareDistribution\Download\*.*") DO rmdir "%%p" /s /q

ipconfig /flushdns