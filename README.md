# Cam Program Splitter

This program splits a CAM program into multiple programs no more than 500 lines of instructions each.

To use it, place the Python script in the same directory as your CAM program, then execute it. The script will walk you through the remaining instructions.

WARNING: If you set the output file name to be 1000 and your current CAM program is 2000 lines long, then the following 4 (2000 / 500 = 4) files will be created and will *overwrite* any files that currently exist with these names:
```
1000.mx2
1001.mx2
1002.mx2
1003.mx2
```
