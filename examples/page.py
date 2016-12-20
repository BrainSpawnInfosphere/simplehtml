#!/usr/bin/env python

from __future__ import print_function
from simplehtml import HTML, CSS


def main():
	# a json file to create the info needed
	data = {
		'Bender.local': {
			'data': [
				['OS', 'Linux Debian Jessie'],
				['cpu', 'ARM'],
				['load', '[1.0, 3.0]'],
				['ram [GB]', 512],
				['uptime', '3 days'],
				['storage [GB]', 3],
				['host', 'bob.local'],
				['IPv4', '127.0.0.1'],
				['MAC', '123456'],
				['Bluetooth', 'Up']
			]
		},
		'Sensors': {
			'header': ['sensor', 'x', 'y', 'z', 'units'],
			'data': [
				['accel [x,y,z]', -1.234, -1.234, -1.234, 'g'],
				['gyros [x,y,z]', -1.234, -1.234, -1.234, 'rad/sec'],
				['mag [x,y,z]', -1.234, -1.234, -1.234, 'telsa'],
				['-', '-', '-', '-', '-'],
				['pos [x,y,z]', 0.1, -2.3, 3.4, 'mm'],
				['vel [x,y,z]', 0.1, -2.3, 3.4, 'mm/sec'],
			]
			# battery, voltage, power, current, run-time, servos-commands (last)
		},
		'Power': {
			'data': [
				['battery [V]', 7.0],
				['current [A]', 3.5]
			]
		},
		# 'Servos': {
		# 	'data': [
		# 		[]
		# 	]
		# }
		'State': {
			'data': [
				['mode', 'idle']
			]
		},
		'Errors': {
			'header': ['system', 'level', 'message'],
			'data': [
				['servos', 'E', 'failed to do something 3.45'],
				['planner', 'W', 'could not get correct path'],
				['kinematics', 'W', 'arc cos: angle out of range [1.2 > 1.0]']
			]
		}

	}

	html = HTML()
	# html.css('img {max-width: 100%;}')
	html.css('h1 {text-align: center;}')
	html.css('img {display: block; margin: 0 auto;}')
	html.css(CSS.cssTable())

	# html.img('https://botsofwesteros.files.wordpress.com/2012/06/banner.jpg', width='100%')
	html.img('https://upload.wikimedia.org/wikipedia/en/a/a6/Bender_Rodriguez.png', width='200px')
	html.h1('Status')

	for key, table in data.items():
		print(key)
		print(table)
		html.h2(key)
		html.table(table)

	html.write('./page.html')


if __name__ == '__main__':
	main()
