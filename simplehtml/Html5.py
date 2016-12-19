#!/usr/bin/env python

"""
A collection of classes to make creating simple dynamic pages easier:

* CSS
* HTML

Example:
	css = '''
		body {
			background-color: white;
		}

		h1 {
			color: black;
			text-align: center;
		}
	'''

	html = HTML()
	html.css(css)
	html.h1('Welcome to my page')
	html.img('mypic.jpg')
	html.p('this is a paragraph about me')
	html.footer('<a href="https://github.com/walchko">my code</a>')
	print html
"""

from Table import Table
from CSS import CSS


# class Base(object):
# 	"""
# 	This is the base class, not sure it is totally useful.
# 	"""
# 	def write(self, filename):
# 		print('need to enable writing')


class HTML(object):
	"""
	This class handles the dynamic contruction of a web page.
	"""
	def __init__(self):
		self.clear()

	def clear(self):
		"""
		Resets the elements of the page back to an empty page.
		"""
		self.parts = ['<!DOCTYPE html>', '<html>', '<head>', '<style>', '</style>', '</head>', '<body>', '</body>', '</html>']

	def css(self, css, bgcolor=None):
		"""
		Given a css, it inserts it into the header of the html page.
		"""
		if bgcolor:
			n = self.find('</style>')
			if n:
				self.parts.insert(n, 'body {background-color: {};}'.format(bgcolor))
		if css:
			n = self.find('</style>')
			if n:
				self.parts.insert(n, css)

	def find(self, token):
		cnt = 0
		for tag in self.parts:
			if tag == token:
				return cnt
				break
			cnt += 1
		return None

	@staticmethod
	def tooltip(text, popup_text):
		return '<div class="tooltip">{}<span class="tooltiptext">{}</span></div>'.format(text, popup_text)

	def linuxFont(self):
		n = self.find('</head>')
		if n:
			self.parts.insert(n, '<link href="https://cdn.rawgit.com/walchko/font-linux/v0.6/assets/font-linux.css" rel="stylesheet">')

	def h1(self, string):
		"""
		Level 1 heading
		"""
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<h1>{}</h1>'.format(string))

	def h2(self, string):
		"""
		Level 2 heading
		"""
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<h2>{}</h2>'.format(string))

	def h3(self, string):
		"""
		Level 3 heading
		"""
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<h3>{}</h3>'.format(string))

	def p(self, string):
		"""
		paragraph
		"""
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<p>{}</p>'.format(string))

	def javascript(self, code):
		"""
		Given the code for some js, it is inserted into the header of the page.
		"""
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<script>{}</script>'.format(code))

	def cssLink(self, css):
		n = self.find('</head>')
		if n:
			self.parts.insert(n, '<link rel="stylesheet" href="{}}">'.format(css))

	def table(self, data):
		n = self.find('</body>')
		if n:
			t = Table()
			t.create(data)
			self.parts.insert(n, str(t))

	def img(self, image, width=None, height=None):
		"""
		Insert an image with optional height and width parameters.
		"""
		n = self.find('</body>')
		if n:
			if width and height:
				self.parts.insert(n, '<img src="{}" alt="img" width="{}" height="{}">'.format(image, width, height))
			elif width:
				self.parts.insert(n, '<img src="{}" alt="img" width="{}">'.format(image, width))
			else:
				self.parts.insert(n, '<img src="{}" alt="img">'.format(image))

	def iframe(self, image, width=None, height=None):
		"""
		Insert an iframe with optional height and width parameters.
		"""
		n = self.find('</body>')
		if n:
			if width and height:
				self.parts.insert(n, '<iframe src="{}" alt="img" width="{}" height="{}">'.format(image, width, height))
			elif width:
				self.parts.insert(n, '<iframe src="{}" alt="img" width="{}">'.format(image, width))
			else:
				self.parts.insert(n, '<iframe src="{}" alt="img">'.format(image))

	def footer(self, string):
		"""
		Insert a footer on your page, you can only have one.
		"""
		n = self.find('</body>')
		if n:
			self.parts.insert(n, '<footer>{}</footer>'.format(string))

	def __str__(self):
		"""
		Returns a string of all of the html elements in the page.
		"""
		return ''.join(self.parts)

	def __repr__(self):
		"""
		Returns a string of all of the html elements in the page.
		"""
		return self.__str__()

	def write(self, filename):
		with open(filename, 'w') as f:
			f.write(self.__str__())


# if __name__ == '__main__':
# 	print 'hello'
