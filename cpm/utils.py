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


