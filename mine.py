#!/usr/bin/python3

def do_create(self, args):
     """ Create an object of any class"""

    if not args:
        print("** class name missing **")
        return

    content = args.split()
    
