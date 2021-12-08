#!/usr/bin/env python3

import os

for dirpath, dirnames, filenames in os.walk("/home/Lemonhead/pythonpros"):
    
    print("Files in %s are:" % dirpath)
    for file in filenames:
        print("\t" + file)

    print("Directories in %s are:" % dirpath)
    for dir in dirnames:
        print("\t" + dir)
