"""
    cpm - Make setup compiling required program easy
    Copyright (C) 2016  thislight

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import json
from os import path
from . import strings
from subprocess import Popen,PIPE

def throw(o):
	raise o

def cpmfile_path(p):
	return path.join(p,strings.CPMFILE)

def cpmfile_exists(p):
	return path.exists(cpmfile_path(p))

def cpmfile(p):
	file_path = cpmfile_path(p)
	package_info = json.load(open(file_path)) if cpmfile_exists(p) else throw(Exception("Could not find cpmfile.json at {}".format(p)))
	# TODO(thislight) a custom exception class
	return package_info

def printex(s,isquiet=False):
	if not isquiet:
		print(s)

def runin_path(x,p):
	return Popen(x, stdout=PIPE, shell=True, cwd=p)


