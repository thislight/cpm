#!/usr/env/bin python3
import sys
import json
import argparse
from os import path
from . import utils
from subprocess import Popen,PIPE


def local_compile(path,quiet=False):
	pk_info = utils.cpmfile(path)
	utils.printex("Compiling {name}...".format(name=pk_info['name']),quiet)
	with utils.runin_path(pk_info['compile'],path) as proc:
		for l in proc.stdout:
			utils.printex("[CompileProcess]: {line}".format(line=l))
		code = proc.wait()
		if code != 0:
			raise Exception("Return code is not zero") # TODO(thislight) CompileException
		else:
			return True


def local_install(path,quiet=False):
	pk_info = utils.cpmfile(path)
	utils.printex("Installing {name}".format(name=pk_info['name']),quiet)
	with utils.runin_path(pk_info['install'],path) as proc:
		for l in proc.stdout:
			utils.printex("[InstallProcess]: {line}".format(line=l))
		code = proc.wait()
		if code != 0:
			raise Excption("Return code is not zero") # TODO(thislight) InstallException
		else:
			return True


def main():
	parser = argparse.ArgumentParser(description="Make compile packages faster. Any code error please open a issue at https://github.com/thislight/cpm")
	parser.add_argument('install',metavar='<path>',nargs='*',type=str,help='paackage path')
	args = parser.parse_args()
	if args.install:
		for v in args.install:
			local_compile(v)
			local_install(v)
	else:
		print("I don't know how can i do.(x o x)")

if __name__ == "__main__":
	main()






