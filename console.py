#!/usr/bin/python3
'''module for console'''


import cmd
import os
import sys

class HBNBCommand(cmd.Cmd):
    '''defines the command line'''

    prompt = '(hbnb) '

    def do_quit(self, line):
        '''exits the program'''
        return True

    def do_EOF(self, line):
        '''exits the programe'''
        return True

    def emptyline(self):
        '''do nothing if line is empty'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
