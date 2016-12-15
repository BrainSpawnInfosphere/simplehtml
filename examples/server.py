#!/usr/bin/env python

from __future__ import print_function
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from socket import gethostname
from Html5 import HTML, CSS


class ServerHandler(BaseHTTPRequestHandler):
	"""
	"""
	def do_GET(self):
		# print 'connection from:', self.address_string()

		if self.path == '/':
			# hn = self.server.server_address[0]
			# pt = self.server.server_address[1]
			# print self.server.server_address

			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			css = """
				body {
					background-color: white;
				}

				h1 {
					color: black;
					text-align: center;
				}

				p {
					font-family: verdana;
					font-size: 20px;
				}

				a:link {
					color: gray;
				}

				a:visited {
					color: gray;
				}

				a:hover {
					color: white;
				}
			"""
			css += CSS.cssTable()
			css += CSS.cssToolTip(400)  # set tooltip box width 400px

			html = HTML()
			html.css(css)
			html.linuxFont()
			html.h1('My Page')
			html.p('hello ... ')
			html.iframe('//giphy.com/embed/4VCevEgXeYzwk', width=300)
			html.h2('header')
			html.p('another paragraph')
			html.image('https://cdn.pixabay.com/photo/2014/03/29/09/17/cat-300572_1280.jpg', width=200)
			html.footer('<a href="https://github.com/walchko">my code</a>')

			self.wfile.write(str(html))
			return

		elif self.path.find('/json') > 0:
			print('looking for json!')

		else:
			print('error', self.path)
			self.send_response(404)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

			html = HTML()
			html.h1('Error: {} not found'.format(self.path))
			self.wfile.write(str(html))
			return


def main():

	try:
		server = HTTPServer((gethostname(), 9000), ServerHandler)
		print("server started")
		server.serve_forever()

	except KeyboardInterrupt:
		print('main interrupt')
		server.socket.close()


if __name__ == '__main__':
	main()
