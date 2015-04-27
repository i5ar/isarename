#!/usr/bin/env python

import os

class iSarename(object):
    '''Rename directories and files'''
    def __init__(self, prev_char, new_char):
        '''Define characters to replace'''
        self.prev_char = prev_char
        self.new_char = new_char

    def rename(self):
        '''Generate the file names'''
        for dirpath, dirnames, filenames in os.walk('.'):
            # Print path to all subdirectories
            for dirname in dirnames:
                print(os.path.join(dirpath, dirname))

            # Print path to all filenames
            for filename in filenames:
                print(os.path.join(dirpath, filename))

            # Stop from recursing into the Git directory
            if '.git' in dirnames:
                dirnames.remove('.git')

            # Rename directories
            print(dirnames)
            for dirname in dirnames:
                new_dirname = dirname.replace (prev_char, new_char)
                os.rename(dirname, new_dirname )

            # Rename files
            print(filenames)
            for filename in filenames:
                new_filename = filename.replace (prev_char, new_char)
                os.rename(filename, new_filename )

# Input characters to replace
# TODO Ask the user if he is sure of this operation
prev_char = str(input("Please, enter the character to replace: ")).lower()
# Input new characters
new_char = str(input("Please, enter the new character: ")).lower()

# User defined exception
class ValueIncorrect(Exception): pass

while True:
   try:
       obj_ref = str(input("Please, enter F for files, D for directories, [B] for both files and directories: ") or 'b').lower()
       if obj_ref != 'f' and obj_ref != 'd' and obj_ref != 'b':
           raise ValueIncorrect
       break
   except ValueIncorrect:
       print("The value is incorrect. Please, try again!")

# Assign characters to replace
rename = iSarename(prev_char, new_char)
rename.rename()
