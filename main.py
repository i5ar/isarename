#!/usr/bin/env python

import os

class iSarename(object):
    '''Rename directories and files'''
    def __init__(self, prev_char, new_char):
        '''Define characters to replace'''
        self.prev_char = prev_char
        self.new_char = new_char
        # Rename files, directories or both
        #self.fdb = fdb

    def rename(self):
        '''Generate the file names'''
        for dirpath, dirnames, filenames in os.walk('.'):
            # Print path to all subdirectories
            for dirname in dirnames:
                print(os.path.join(dirpath, dirname))

            # Print path to all filenames
            for filename in filenames:
                print(os.path.join(dirpath, filename))

            # Rename directories
            print(dirnames)
            for dirname in dirnames:
                if ' ' in dirname:
                    # Replace space with underscore
                    new_dirname = dirname.replace (prev_char, new_char)
                    os.rename(dirname, new_dirname )

            # Rename files
            print(filenames)
            for filename in filenames:
                if ' ' in filename:
                    # Replace space with underscore
                    new_filename = filename.replace (prev_char, new_char)
                    os.rename(filename, new_filename )

#prev_char = ' '
#new_char = '_'
#fdb = '_'

while True:
    try:
        prev_char = str(input("Please, enter the character to replace [SPACE]: ") or ' ')
        break
    except ValueError:
        print("That wasn't a valid character(s). Please, try again: ")

while True:
    try:
        new_char = str(input("Please, enter the new character [UNDERSCORE]: ") or '_')
        break
    except ValueError:
        print("That wasn't a valid character(s). Please, try again: ")

''' Choose files, directories or both
while True:
    try:
        fdb = str(input("Rename Files, Directory or [B]oth? ") or 'b').lower()
        if fdb == 'f' or fdb == 'd' or fdb == 'b':
            break
        else:
            print("That wasn't a valid character(s). Please, try again!")
    except ValueError:
        print("That wasn't a valid character(s). Please, try again: ")
'''

rename = iSarename(prev_char, new_char)
rename.rename()
