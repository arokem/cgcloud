#!/usr/bin/env python2.7

import os

import sys

sys.path.append( os.path.join( os.path.dirname( __file__ ), 'src' ) )

from cgcloud.core.cli import main

if __name__ == "__main__":
    main( )
