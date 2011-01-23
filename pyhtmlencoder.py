#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Copyright 2011 Francisco Canela González
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

"""
Example script that encode HTML tildes
"""
import sys
import os.path
import re

# Application needs one parameter.
if (len(sys.argv) != 3):
    print "Usage: ./pyhtmlencode.py <input> <output>"
else:
    print "[+] Encoding the document..."
    # Open the files and read the input
    if (os.path.isfile(sys.argv[1]) == False):
        print "[!] Input file does not exist!"
        sys.exit(-1)
    finput = open(sys.argv[1], "r")
    fdata = finput.read()
    finput.close()

    # Lower case tilde
    fdata = re.sub("á", "&aacute;", fdata)
    fdata = re.sub("é", "&eacute;", fdata)
    fdata = re.sub("í", "&íacute;", fdata)
    fdata = re.sub("ó", "&oacute;", fdata)
    fdata = re.sub("ú", "&uacute;", fdata)
    # Upper case tilde
    fdata = re.sub("Á", "&Aacute;", fdata)
    fdata = re.sub("É", "&Eacute;", fdata)
    fdata = re.sub("Í", "&Iacute;", fdata)
    fdata = re.sub("Ó", "&Oacute;", fdata)
    fdata = re.sub("Ú", "&Úacute;", fdata)
    # Lower case umlaut
    fdata = re.sub("ä", "&auml;", fdata)
    fdata = re.sub("ë", "&euml;", fdata)
    fdata = re.sub("ï", "&iuml;", fdata)
    fdata = re.sub("ö", "&ouml;", fdata)
    fdata = re.sub("ü", "&uuml;", fdata)
    # Upper case umlaut
    fdata = re.sub("Ä", "&Auml;", fdata)
    fdata = re.sub("Ë", "&Euml;", fdata)
    fdata = re.sub("Ï", "&Iuml;", fdata)
    fdata = re.sub("Ö", "&Ouml;", fdata)
    fdata = re.sub("Ü", "&Uuml;", fdata)
    # Spanish "ñ"
    fdata = re.sub("ñ", "&ntilde;", fdata)
    fdata = re.sub("Ñ", "&Ntilde;", fdata)
    # Spanish exclamation and interrogation
    fdata = re.sub("¡", "&iexcl;", fdata)
    fdata = re.sub("¿", "&iquest;", fdata)

    # Save the changes
    foutput = open(sys.argv[2], "w")
    foutput.write(fdata)
    foutput.close()
    print "[+] Document encoded!"
