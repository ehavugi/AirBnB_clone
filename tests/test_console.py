#!/usr/bin/python3
"""
HHNB Console unit tests

"""
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help all")

