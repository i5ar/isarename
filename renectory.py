#!/usr/bin/env python

import os

class dirWalk(object):
    def __init__(self):
        '''Get directory path name'''
        self.dir_name = str(input('Please, insert the directory path or press Enter for the current directory: ') or '.')
