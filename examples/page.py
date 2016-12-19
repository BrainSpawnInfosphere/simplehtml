#!/usr/bin/env python

from __future__ import print_function
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# from socket import gethostname
from simplehtml import HTML, CSS


def main():
	# a json file to create the info needed
	data = {
		'linux': {
			'data': [
				['cpu', '[1.0, 3.0]'],
				['ram', 512, 'GB'],
				['storage', 3, 'GB']
			]
		},
		'robot': {
			'header': ['sensor', 'x', 'y', 'z', 'units'],
			'data': [
				['accel [x,y,z]', -1.234, -1.234, -1.234, 'g'],
				['gyros [x,y,z]', -1.234, -1.234, -1.234, 'rad/sec'],
				['mag [x,y,z]', -1.234, -1.234, -1.234, '?'],
				['-----------------'],
				['pos [x,y,z]', 0.1, -2.3, 3.4, 'mm'],
				['vel [x,y,z]', 0.1, -2.3, 3.4, 'mm/sec'],
			]
		}
	}

	html = HTML()
	html.css('img {max-width: 100%;}')
	html.css('h1 {text-align: center;}')
	html.css(CSS.cssTable())
	
	html.img('https://botsofwesteros.files.wordpress.com/2012/06/banner.jpg')
	html.h1('Status')

	for key, table in data.items():
		print(key)
		print(table)
		html.h2(key)
		html.table(table)

	html.write('./page.html')


if __name__ == '__main__':
	main()
