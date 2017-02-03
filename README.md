# cpm

[![Join the chat at https://gitter.im/cpm-project/Lobby](https://badges.gitter.im/cpm-project/Lobby.svg)](https://gitter.im/cpm-project/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Make compilation easy

## Quick Start
> cpm still alpha, you can install it from code.

Package Required:
- git
- python (>=3.4)

Run in shell if you are using *unix:

````
git clone https://github.com/thislight/cpm.git
cd cpm
sudo python3 setup.py install # If you aren't using root user.
````


Run in cmd if you are using Windows:

````
git clone https://github.com/thislight/cpm.git
cd cpm
python setup.py install
````

If you are update cpm from old version:

````
git clone https://github.com/thislight/cpm.git
cd cpm
sudo cpm install
````

Use `cpm -h` to verify that it is installed correctly

## How to use
`cpm install [[<path>] <path>...]` install some packages.

Example:
````
$ sudo cpm install .
Compiling python...
[...]
Installing python...
[...]
````
Well, you can use `cpm install`, it mean `cpm install .`.


`cpm compile [<path> [<path>...]]` compile some packages.

Example:
````
$ cpm compile .
Compiling python...
[...]
````
Well, you can use `cpm compile`, it mean `cpm compile .`.


`cpm module xxx` or `cpm %xxx` run some modules of *cpmfile.json*.

Example:
````
$ cpm module xxx
[...]
$ cpm %xxx
[...]
````
They run cpm with current path.


cpm will read *cpmfile.json* to get infomation.  
A basic cpmfile.json example:
````json
{
	"name": "python",
	"compile": "./configure;make",
	"install": "make install"
}
````

## License
GNU GPL v3

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
