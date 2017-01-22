from setuptools import setup


VERSION = "0.1.0-alpha"


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
