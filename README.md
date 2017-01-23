# cpm
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

Use `cpm -h` to verify that it is installed correctly

## How to use
`cpm [[<path>] <path>...]` to install some packages.

Example:
````
# cpm Python-3.6.0
Installing python
[...]
````
cpm will read \<path\>/cpmfile.json to get infomation.
A basic cpmfile.json example:
````json
{
	"name": "python",
	"compile": "./configure;make",
	"install": "make install"
}
````

## License
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
