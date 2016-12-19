

class Table(object):
	"""
	Create a simple table from a json object.

	info = {
		"header": [5, 6, 7],
		"data": [
			["hello", "hi", "ola"],
			[1, 2, 3],
			["a", "b", "c"]
		],
		'class': 'my_cool_class'
	}

	t = Table()
	t.create(info)
	print t
	"""
	def __init__(self):
		self.table = []

	def create(self, data):
		"""
		Create a simple table from a json object.
		"""
		if 'class' in data:
			self.table.append('<table class={}>'.format(data['class']))
		else:
			self.table.append('<table>')

		if 'header' in data:
			self.table.append('<tr>')
			for hdr in data['header']:
				s = str(hdr)
				self.table.append('<th>' + s + '</th>')
			self.table.append('</tr>')

		for line in data['data']:
			s = map(str, line)
			l = '<tr>'
			for i in s:
				l += '<td>' + i + '</td>'
			l += '</tr>'
			self.table.append(l)
		self.table.append('</table>')

	def __str__(self):
		"""
		Returns a string of all of the html elements in the page.
		"""
		return ''.join(self.table)

	def __repr__(self):
		"""
		Returns a string of all of the html elements in the page.
		"""
		return self.__str__()
