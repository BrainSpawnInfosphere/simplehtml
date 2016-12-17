__version__ = '0.2.0'

from Html5 import HTML, CSS, Table
# from pwn import readJson, writeJson, isBreach
# from server import PwmThread, ServerHandler
try:
	import simplejson as json
except:
	import json


def readJson(fname):
	"""
	Reads a Json file
	in: file name
	out: length of file, dictionary
	"""
	try:
		with open(fname, 'r') as f:
			data = json.load(f)

		return data
	except IOError:
		raise Exception('Could not open {0!s} for reading'.format((fname)))


def writeJson(fname, data):
	"""
	Writes a Json file
	"""
	try:
		with open(fname, 'w') as f:
			json.dump(data, f)

	except IOError:
		raise Exception('Could not open {0!s} for writing'.format((fname)))
