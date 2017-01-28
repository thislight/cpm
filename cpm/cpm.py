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


def run(path,what,modc=None):
    info = utils.cpmfile(path)
    mod_name = utils.module_name(what,modc)
    cmd = info.get(mod_name,None)
    if not cmd:
        return False,None
    proc = utils.run_module(info,mod_name,path)
    return proc,info


def local_compile(path,modc=None,quiet=False):
    p,info = run(path,'compile',modc)
    if not p:
        utils.printex('Compile passed, compile module is empty.',quiet)
        return True
    utils.printex("Compiling {name}...".format(name=utils.p_name(info)),quiet)
    with p as proc:
        for l in proc.stdout:
            utils.printex("[CompileProcess]: {line}".format(line=l),quiet)
        code = proc.wait()
        if code != 0:
            raise errors.CompileException("Return code is not zero")
        else:
            utils.printex("Compile complete",quiet)
            return True


def local_install(path,modc=None,quiet=False):
    p,info = run(path,'install',modc)
    utils.printex("Installing {name}...".format(name=utils.p_name(info)),quiet)
    with p as proc:
        for l in proc.stdout:
            utils.printex("[InstallProcess]: {line}".format(line=l),quiet)
        code = proc.wait()
        if code != 0:
            raise errors.InstallExcption("Return code is not zero")
        else:
            utils.printex("Install complete",quiet)
            return True


def install_helper(*args,**kargs):
    local_compile(*args,**kargs)
    local_install(*args,**kargs)


def main():
    parser = argparse.ArgumentParser(description="Make compiling packages faster. Any code error please open a issue at https://github.com/thislight/cpm")
    parser.add_argument('op',metavar='<op.>',choices=['install','compile','module'],type=str,help='choices: install,compile,module')
    parser.add_argument('--module','-m',default=None,type=str,help='Run a module',dest='module')
    parser.add_argument('args',metavar='<args>',nargs='*',default='.',type=str,help='args')
    parser.add_argument('--quiet','-q',action='store_true',default=False,help='Stop print infomation',dest='isquiet')
    args = parser.parse_args()
    # ...
    utils.printex('Please wait...',args.isquiet)
    if args.op == "install":
        for v in args.args:
            install_helper(v,quiet=args.isquiet,modc=args.module)
    elif args.op == "compile":
        for v in args.args:
            local_compile(v,quiet=args.isquiet,modc=args.module)
    elif args.op == "module":
        for v in args.args:
            utils.printall(run('.',v,args.module)[0].stdout,args.isquiet)
    else:
        print("I don't know how can i do.(x o x)")


def __main__():
    main()

if __name__ == "__main__":
    main()
