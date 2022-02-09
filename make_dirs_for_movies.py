#! /usr/bin/python
# -*- coding: utf8 -*-

import os, sys
from path import path



def main(args):
    folder, keyword = path(args[0]), args[1]

    if not folder.exists() and folder.isdir():
        print str(folder) + " is not a valid folder path."
        exit(1)
    targets = []
    for fpath in folder.files():
        if keyword.lower() in fpath.basename().lower():
            targets.append(fpath)
    if targets:
        new_dir = folder / keyword
        new_dir.makedirs_p()
        if new_dir.exists() and new_dir.isdir():
            for fpath in targets:
                dest = new_dir / fpath.basename()
                print "moving {} to {}".format(str(fpath), dest)
                fpath.move(new_dir)
    else:
        msg = "No files in {} match the keyword {}."
        print msg.format(repr(str(folder)), repr(keyword))

if __name__ == "__main__":
    args = sys.argv[1:]
    help = ('-h', '--help', '/h', '/help', '/?')
    if len(args) != 2 or args[0] in help or args[1] in help:
        print "Moves files in <path> whose name matches <keyword> into a"
        print "subdirectory of <path> named <keyword>"
        print "Usage:"
        print "{} <path> <keyword>".format(sys.argv[0])
        exit(0)
    try:
        main(args)
    except OSError, err:
        print "Failed: " + err.strerror