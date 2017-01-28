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
from setuptools import setup


VERSION = "0.1.2-alpha"


setup(
	name="cpm",
	version=VERSION,
	author="thislight",
	author_email="l1589002388@gmail.com",
	packages=['cpm'],
	entry_points="""
	[console_scripts]
	cpm = cpm.cpm:main
	"""
	)
