#!/usr/env/bin python3
"""
    cpm - Make compilation easy
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
import sys
import json
import argparse
from os import path
from . import utils
from . import errors
from subprocess import Popen,PIPE


def local_compile(path,quiet=False):
    pk_info = utils.cpmfile(path)
    if utils.is_str_empty(pk_info.get('compile',None)):
        utils.printex('Compile passed, compile module is empty.',quiet)
        return True
    utils.printex("Compiling {name}...".format(name=pk_info['name']),quiet)
    with utils.runin_path(pk_info['compile'],path) as proc:
        for l in proc.stdout:
            utils.printex("[CompileProcess]: {line}".format(line=l),quiet)
        code = proc.wait()
        if code != 0:
            raise errors.CompileException("Return code is not zero")
        else:
            utils.printex("Compile complete",quiet)
            return True


def local_install(path,quiet=False):
    pk_info = utils.cpmfile(path)
    utils.printex("Installing {name}...".format(name=pk_info['name']),quiet)
    with utils.runin_path(pk_info['install'],path) as proc:
        for l in proc.stdout:
            utils.printex("[InstallProcess]: {line}".format(line=l),quiet)
        code = proc.wait()
        if code != 0:
            raise errors.InstallExcption("Return code is not zero")
        else:
            utils.printex("Install complete",quiet)
            return True


def main():
    parser = argparse.ArgumentParser(description="Make compiling packages faster. Any code error please open a issue at https://github.com/thislight/cpm")
    parser.add_argument('op',metavar='<op.>',choices=['install','compile'],type=str,help='choices: install,compile')
    parser.add_argument('path',metavar='<path>',nargs='*',default='.',type=str,help='path')
    parser.add_argument('--quiet','-q',action='store_true',default=False,help='Stop print infomation',dest='isquiet')
    args = parser.parse_args()
    # ...
    utils.printex('Please wait...',args.isquiet)
    if args.op == "install":
        for v in args.path:
            local_compile(v,args.isquiet)
            local_install(v,args.isquiet)
    elif args.op == "compile":
        for v in args.path:
            local_compile(v,args.isquiet)
    else:
        print("I don't know how can i do.(x o x)")


def __main__():
    main()

if __name__ == "__main__":
    main()
