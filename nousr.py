#!/usr/bin/env python3

import os
import os.path

#first create a set to check all of the user ids in passwd file. 
uidset = set() #set is unordered set of unique options we are testing to see if a specific value is member of the set.

for line in open("/etc/passwd"): #loop is scanning the passwd file for what we want in the set above.
    split = line.split(":")
    uidset.add(int(split[2]))

#an easy way using a pwd module is :
##import pwd
##uidset = set()
##for user in pwd.getpwall():#this way will pick up accounts in LDAP or AD
##    uidset.add(user.pw_uid)

#walk the sepcified dir
testdir = "/home/Lemondhead"

for folder, dirs, files in os.walk(testdir):
    for file in files:
        #build the full pathname of file.
        path = folder + "/" + file
##        if os.path.islink(path):
##            print(path + " is a symlink ... skipping")
##          continue

        try:
            attributes = os.stat(path)
        except FileNotFoundError:
            #this will occur if we encounter broken symlink
            print(path + "not found")
            continue

        if attributes.st_uid not in uidset:
            print(path + "has no owne")
