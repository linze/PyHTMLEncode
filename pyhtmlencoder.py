#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Copyright 2011 Francisco Canela González
		   Adrián Pérez Heredia
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

def check_inputfile():
    
    if(os.path.isfile(sys.argv[1]) == False):
        print("[!] Input file does not exist!")
        sys.exit(-1)

def create_dict():
    
    d = dict()
    
    #Lower case Acute accent
    d["á"] = "&aacute;"
    d["é"] = "&eacute;"
    d["í"] = "&iacute;"
    d["ó"] = "&oacute;"
    d["ú"] = "&uacute;"

    #Upper case Acute accent
    d["Á"] = "&Aacute;"
    d["É"] = "&Eacute;"
    d["Í"] = "&Iacute;"
    d["Ó"] = "&Oacute;"
    d["Ú"] = "&Uacute;"

    #Lower case umlaut
    d["ä"] = "&auml;"
    d["ë"] = "&euml;"
    d["ï"] = "&iuml;"
    d["ö"] = "&ouml;"
    d["ü"] = "&uuml;"

    #Upper case umlaut
    d["Ä"] = "&Auml;"
    d["Ë"] = "&Euml;"
    d["Ï"] = "&Iuml;"
    d["Ö"] = "&Ouml;"
    d["Ü"] = "&Uuml;"

    # "ñ" character
    d["ñ"] = "&ntilde;"
    d["Ñ"] = "&Ntilde;"

    # Spanish exclamation and interrogation
    d["¡"] = "&iexcl;"
    d["¿"] = "&iquest;"

    return d

def do_encoding(dic, output_file):
    
    finput = open(sys.argv[1], "r")
    fdata = finput.read()
    finput.close()
    
    it = dic.iterkeys()
    
    print("[+] Encoding document...")

    for key in it:
        fdata = re.sub(key,dic.get(key), fdata)

    foutput = open(output_file, "w")
    foutput.write(fdata)
    foutput.close()

    print("[+] Document encoded !")


def encode(output_file):
    
    check_inputfile()
    dic = create_dict()
    do_encoding(dic, output_file)

#Entry point
if(len(sys.argv) > 3 or len(sys.argv) < 2):
    
    print("Usage: htmlenc <input> [<output>]")

else:
    
    #If only input file is specified, it will be used as output too.

    if(len(sys.argv) != 3):
        output_file = sys.argv[1]
    else:
        output_file = sys.argv[2]

    encode(output_file)
    sys.exit(0)


