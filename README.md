# IOURS
 Idle Online Universe Runes Solver

Math based on Multicalc v10.0.3

# Usage
### One level
If you want to check best rune for one specific level, choose 'One level' in Opponent Data Input. A simple message box will give you information about best rune combination and needed heals to win.

### Continuous
If you want to check what runes are best in the long run, choose this option. From given level, up to 'Limit', one best rune per 10 levels is chosen. Then heals for every level for all this runes are calculated. As rune level 30 can have 4 bonuses, 2x rune lvl 30 gives 1679616 combination. Multiply this by 4 (Limit 40) and it gets quite large, so it can take some time, be patient.

# Compilation
1. Requirements
````
matplotlib==3.4.1
pyinstaller==4.3
pywin32-ctypes==0.2.0
````

2. DLL

DLL must be compiled with MSVC
````
"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat" && "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29910\bin\Hostx64\x64\cl.exe" /LD /O2 fight.c -DBUILD_DLL /link
````
Paths to vcvars64.bat and cl.exe may vary.

3. EXE
````
pyinstaller -F main.py
````
