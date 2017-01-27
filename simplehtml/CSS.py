
#
# class CSS(object):
# 	"""
# 	This class helps with some html css parameters.
# 	"""
# 	@staticmethod
# 	def basic():
# 		"""
# 		Returns a simple css.
# 		"""
# 		basic = """
# 		body {
# 			background-color: white;
# 		}
#
# 		h1 {
# 			color: black;
# 			text-align: center;
# 		}
#
# 		p {
# 			font-family: verdana;
# 			font-size: 20px;
# 		}
# 		"""
# 		return basic
#
# 	@staticmethod
# 	def cssTable(color='#dddddd'):
# 		"""
# 		A simple table css that alternates the color of every other row by
# 		a use defined color (the default is gray).
# 		"""
# 		css = """
# 		table {
# 			font-family: arial, sans-serif;
# 			border-collapse: collapse;
# 			width: 100%;
# 			}
# 		td, th {
# 			border: 1px solid #dddddd;
# 			text-align: left;
# 			padding: 8px;
# 		}
# 		tr:nth-child(even) {
# 			background-color: COLOR;
# 		}"""
# 		return css.replace('COLOR', color)
#
# 	@staticmethod
# 	def cssToolTip(width=200):
# 		"""
# 		Css parameters to have a nice tool tip popup box of a user defined
# 		width (default is 200px).
# 		"""
# 		css = """
# 		.tooltip {
# 			position: relative;
# 			display: inline-block;
# 			border-bottom: 1px dotted black;
# 		}
#
# 		.tooltip .tooltiptext {
# 			visibility: hidden;
# 			width: TEXT_WIDTH;
# 			background-color: #555;
# 			color: #fff;
# 			text-align: center;
# 			border-radius: 6px;
# 			padding: 5px 0;
# 			position: absolute;
# 			z-index: 1;
# 			bottom: 125%;
# 			left: 50%;
# 			margin-left: TEXT_OFFSET;
# 			opacity: 0;
# 			transition: opacity 1s;
# 		}
#
# 		.tooltip .tooltiptext::after {
# 			content: "";
# 			position: absolute;
# 			top: 100%;
# 			left: 50%;
# 			margin-left: -5px;
# 			border-width: 5px;
# 			border-style: solid;
# 			border-color: #555 transparent transparent transparent;
# 		}
#
# 		.tooltip:hover .tooltiptext {
# 			visibility: visible;
# 			opacity: 1;
# 		}
# 		"""
# 		css = css.replace('TEXT_WIDTH', str(width)+'px')
# 		css = css.replace('TEXT_OFFSET', str(-width/2)+'px')
# 		# css = css.replace('TEXT_WIDTH', '400px')
# 		# css = css.replace('HALF_TEXT_WIDTH', '-400px')
# 		return css


class cssStripedTable(object):
	@staticmethod
	def get(self, color='#dddddd'):
		"""
		A simple table css that alternates the color of every other row by
		a use defined color (the default is gray).
		"""
		css = """
		table {
			font-family: arial, sans-serif;
			border-collapse: collapse;
			width: 100%;
			}
		td, th {
			border: 1px solid #dddddd;
			text-align: left;
			padding: 8px;
		}
		tr:nth-child(even) {
			background-color: COLOR;
		}"""
		return css.replace('COLOR', color)


class cssToolTip(object):
	@staticmethod
	def get(width=200):
		"""
		Css parameters to have a nice tool tip popup box of a user defined
		width (default is 200px).
		"""
		css = """
		.tooltip {
			position: relative;
			display: inline-block;
			border-bottom: 1px dotted black;
		}

		.tooltip .tooltiptext {
			visibility: hidden;
			width: TEXT_WIDTH;
			background-color: #555;
			color: #fff;
			text-align: center;
			border-radius: 6px;
			padding: 5px 0;
			position: absolute;
			z-index: 1;
			bottom: 125%;
			left: 50%;
			margin-left: TEXT_OFFSET;
			opacity: 0;
			transition: opacity 1s;
		}

		.tooltip .tooltiptext::after {
			content: "";
			position: absolute;
			top: 100%;
			left: 50%;
			margin-left: -5px;
			border-width: 5px;
			border-style: solid;
			border-color: #555 transparent transparent transparent;
		}

		.tooltip:hover .tooltiptext {
			visibility: visible;
			opacity: 1;
		}
		"""
		css = css.replace('TEXT_WIDTH', str(width)+'px')
		css = css.replace('TEXT_OFFSET', str(-width/2)+'px')
		return css
