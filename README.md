# Cam Program Splitter

This was needed for an older style of control for a Prototrak M2, which limits the event size to 500 events.

This python script splits a CAM program into multiple programs into 500 lines or less of G-code lines each.

To start: Ensure Python 3.12 is installed by installing this: https://apps.microsoft.com/detail/9NCVDN91XZQP?hl=en-us&gl=US.

To use it, place the Python script in the same directory as your CAM program, then execute it. The script will walk you through the remaining instructions.

**Note:** Since this program was written for an M2 prototrak control, which means there is no Z-Axis CNC motor, just a DRO. As such, this script looks for any Z-Axis moves and outputs all locations where it found a Z-Axis move (useful for 2 Axis only, 3 Axis can ignore this!).

**WARNING:** If you set the output file name to be 1000 and your current CAM program is 2000 lines long, then the following 4 (2000 / 500 = 4) files will be created and will **overwrite** any files that currently exist with these names:
```
1000.mx2
1001.mx2
1002.mx2
1003.mx2
```

