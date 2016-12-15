import os
from setuptools import setup, find_packages
from simplehtml import __version__ as VERSION
from setuptools.command.test import test as TestCommand


class NoseTestCommand(TestCommand):
	pass
	# def run_tests(self):
	# 	print('Running nose tests ...')
	# 	os.system('nosetests -v test/test.py')


class PublishCommand(TestCommand):
	def run_tests(self):
		print('Publishing to PyPi ...')
		os.system("python setup.py bdist_wheel")
		# os.system("twine upload dist/pygecko-{}.tar.gz".format(VERSION))
		os.system("twine upload dist/simplehtml-{}*.whl".format(VERSION))


class GitTagCommand(TestCommand):
	def run_tests(self):
		print('Creating a tag for version {} on git ...'.format(VERSION))
		os.system("git tag -a {} -m 'version {}'".format(VERSION, VERSION))
		os.system("git push --tags")


class CleanCommand(TestCommand):
	def run_tests(self):
		print('Cleanning up ...')
		os.system('rm -fr simplehtml.egg-info dist build')

readme = open('README.rst').read()

setup(
	name="simplehtml",
	version=VERSION,
	author="Kevin Walchko",
	keywords=['html', 'security'],
	author_email="kevin.walchko@outlook.com",
	description="A simple html generation",
	license="MIT",
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 2 :: Only',
		'Operating System :: Unix',
		'Operating System :: POSIX :: Linux',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX',
		# 'Topic :: Scientific/Engineering',
		# 'Topic :: Scientific/Engineering :: Artificial Intelligence',
		# 'Topic :: Scientific/Engineering :: Image Recognition',
		# 'Topic :: Software Development :: Libraries :: Python Modules',
	],
	install_requires=[
		'requests',
		'simplejson'
	],
	url="https://github.com/walchko/simplehtml",
	long_description=readme,
	packages=['simplehtml'],
	# packages=find_packages(),
	cmdclass={
		'test': NoseTestCommand,
		'publish': PublishCommand,
		'tag': GitTagCommand,
		'clean': CleanCommand
	},
	# scripts=[
	# 	'chi/tools/mjpeg-server.py'
	# ]
	# entry_points={
	# 	'console_scripts': [
	# 		'pwnserver=pwn.server:main',
	# 	],
	# },
)
