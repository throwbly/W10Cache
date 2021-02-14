del /q "C:\Users\fiedo\AppData\Local\Temp\*"
del /q "C:\Windows\Temp\*"
del /q "C:\Windows\Prefetch\*"
del /q "%userprofile%\AppData\Local\Spotify\Data\*"
del /q "%userprofile%\AppData\Local\NVIDIA\GLCache\*"
del /q "C:\ProgramData\NVIDIA Corporation\NV_Cache\*"
del /q "C:\Windows\SoftwareDistribution\Download\*"

FOR /D %%p IN ("%userprofile%\AppData\Local\Temp\*.*") DO rmdir "%%p" /s /q
FOR /D %%p IN ("C:\Windows\Temp\*.*") DO rmdir "%%p" /s /q
FOR /D %%p IN ("C:\Windows\Prefetch\*.*") DO rmdir "%%p" /s /q
FOR /D %%p IN ("%userprofile%\AppData\Local\Spotify\Data\*.*") DO rmdir "%%p" /s /q
FOR /D %%p IN ("%userprofile%\AppData\Local\NVIDIA\GLCache\*.*") DO rmdir "%%p" /s /q
FOR /D %%p IN ("C:\ProgramData\NVIDIA Corporation\NV_Cache\*.*") DO rmdir "%%p" /s /q
FOR /D %%p IN ("C:\Windows\SoftwareDistribution\Download\*.*") DO rmdir "%%p" /s /q

ipconfig /flushdns
WSReset.exe