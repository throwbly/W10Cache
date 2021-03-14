up = '%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs'
pd = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs'

ls = {
        'Windows Menu USELESS FOLDERS' : [
            f'{pd}\\Accessibility\\*',
            f'{up}\\Accessibility\\*',
            f'{pd}\\System Tools\\*',
            f'{up}\\System Tools\\*',
            f'{pd}\\Administrative Tools\\*',
            f'{pd}\\Accessories\\*',
            f'{up}\\Windows PowerShell\\*',
            f'{pd}\\Microsoft Office Tools\\*',
            f'{pd}\\Accessories\\System Tools\\Character Map.lnk'
        ],
        
        'Windows bin in program files' : [
            r'C:\\Program Files\\Internet Explorer',
            r'C:\\Program Files\\Windows Mail',
            r'C:\\Program Files\\Windows NT',
            r'C:\\Program Files\\Windows Photo Viewer',
            r'C:\\Program Files\\WindowsPowerShell',
            r'C:\\Program Files (x86)\\Windows Mail',
            r'C:\\Program Files (x86)\\Windows NT',
            r'C:\\Program Files (x86)\\Windows Photo Viewer',
            r'C:\\Program Files (x86)\\WindowsPowerShell',
            r'%USERPROFILE%\\Links',
            r'%USERPROFILE%\\3D Objects',
            r'%USERPROFILE%\\OneDrive',
            r'%USERPROFILE%\\Favorites',
            r'%USERPROFILE%\\Videos',
            r'%USERPROFILE%\\Searches',
            r'%USERPROFILE%\\Saved Games',
            r'%USERPROFILE%\\Contacts',
            r'%USERPROFILE%\\Documents\\Niestandardowe szablony pakietu Office',
            r'C:\\Users\\Kacper\Pictures\\Camera Roll',
            r'C:\\Users\\Kacper\\Pictures\\Saved Pictures',
            r'C:\\Users\\Kacper\\Videos\\Captures',
            r'C:\\Users\\Public',
            r'C:\\Users\\Kacper\Music'
        ]
     }

toClean = [
    '%temp%'
]

reg = {
    'Desktop' : [
        '{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}'
    ],

    'Documents' : [
        '{A8CDFF1C-4878-43be-B5FD-F8091C1C60D0}',
        '{d3162b92-9365-467a-956b-92703aca08af}'
    ],

    'Video' : [
        '{A0953C92-50DC-43bf-BE83-3742FED03C9C}',
        '{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}'
    ],

    'Pictures' : [
       '{3ADD1653-EB32-4cb0-BBD7-DFA0ABB5ACCA}',
       '{24ad3ad4-a569-4530-98e1-ab02f9417aa8}'
    ],

    'Downloads' : [
        '{374DE290-123F-4565-9164-39C4925E467B}',
        '{088e3905-0323-4b02-9826-5d99428e115f}'
    ],

    'Music' : [
        '{1CF1260C-4DD0-4ebb-811F-33C572699FDE}',
        '{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}'
    ]
}