#!/usr/bin/env python

import os
import renectory

# Get directory path name
dir_name = renectory.dirWalk().dir_name

# User defined exception
class ValueIncorrect(Exception): pass

class iSarename(object):
    '''Rename directories and files'''
    def __init__(self):
        '''Define characters to replace'''
        self.prev_char = str(input("Please, enter the character to replace or press Enter in order to replace the [SPACE]") or ' ').lower()
        self.new_char = str(input("Please, enter the new character: ")).lower()
        # Assign files and folders
        while True:
           try:
               self.obj_ref = str(input("Please, enter F for files, D for directories, [B] for both files and directories: ") or 'b').lower()
               if self.obj_ref != 'f' and self.obj_ref != 'd' and self.obj_ref != 'b':
                   raise ValueIncorrect
               break
           except ValueIncorrect:
               print("The value is incorrect. Please, try again!")

    def rename(self):
        '''Generate the file names'''
        for dirpath, dirnames, filenames in os.walk(dir_name):
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
            if self.obj_ref == 'd' or self.obj_ref == 'b':
                print(dirnames)
                for dirname in dirnames:
                    # Replace previous character(s) directory name with new character(s)
                    new_dirname = dirname.replace (self.prev_char, self.new_char)
                    os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, new_dirname))

            # Rename files
            if self.obj_ref == 'f' or self.obj_ref == 'b':
                print(filenames)
                for filename in filenames:
                    # Replace previous character(s) file name with new character(s)
                    new_filename = filename.replace (self.prev_char, self.new_char)
                    os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))

class iSelp(object):
    def __init__(self, option):
        self.option = option

    def help(self):
        print('Enter \'help\' or \'-h\' to ask help')
        print('Enter \'lower\' to lowercase')
        print('Enter \'rename\' to rename')
        print('Enter \'reduce\' to reduce')

class iSower(object):
    '''Lower file names'''
    def __init__(self):
        print('Lower file names')

    def lower(self):
        for dirpath, dirnames, filenames in os.walk(dir_name):

            # Stop from recursing into the Git directory
            if '.git' in dirnames:
                dirnames.remove('.git')

            # Rename files
            print(filenames)
            for filename in filenames:
                new_filename = filename.lower()
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))

class iSareduce(object):
    '''Reduce number file names'''
    def __init__(self):
        print('Reduce number file names')

    def reduce(self):
        '''Reduce number file names'''
        for dirpath, dirnames, filenames in os.walk(dir_name):

            # Stop from recursing into the Git directory
            if '.git' in dirnames:
                dirnames.remove('.git')

            # Get max length
            length = []
            for filename in filenames:
                basename = os.path.splitext(filename)[0]
                length.append(len(basename))
            max_length = max(length)

            # TODO Use filename reverse to increase instead of reduce
            filenames_reverse = sorted(filenames, reverse=True)

            # Reduce
            for filename in filenames:
                # Remove extension from the file name
                basename = os.path.splitext(filename)[0]
                # Reduce number base name
                new_basename = str(int(basename)-1).zfill(max_length)
                # Add extension to the base name
                new_filename = new_basename + os.path.splitext(filename)[1]
                # Rename
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))

class iSoption():
    '''Choose options'''
    def __init__(self):
        self.option = str(input("Please, enter an option or press Enter: ") or 'help').lower()

# Loop while 'help' option
option = iSoption().option
while option != 'exit':
    if option == 'help' or option == '-h':
        iSelp(option).help()
    if option == 'lower':
        iSower().lower()
        break
    if option == 'rename':
        iSarename().rename()
        break
    if option == 'reduce':
        iSareduce().reduce()
        break
    option = iSoption().option
