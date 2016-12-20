from __future__ import division
import matplotlib.pyplot as plt
# import numpy as np
import mpld3
from math import cos, sin, pi

"""
A simple example using mpld3 to create webpages with matplotlib graphs on it.
It only creates the webpage and then prints it to standard out, however, you
could do a lot more with it like stick the html into a div().
"""


fig, ax = plt.subplots()
N = 100

x = []
y = []
y2 = []
y3 = []

for i in range(0, 600):
	xx = float(i)
	yy = 5.0*cos(2.0*pi*i/200)
	yy2 = yy*sin(2.0*pi*i/300)
	yy3 = 3.5*cos(2.0*pi*i/100)+2.0*sin(2.0*pi*i/300)
	x.append(xx)
	y.append(yy)
	y2.append(yy2)
	y3.append(yy3)

scatter = ax.plot(x, y, x, y2, x, y3)
# ax.grid(color='white', linestyle='solid')
ax.grid(True)
ax.set_title("Test", size=20)

# labels = ['point {0}'.format(i + 1) for i in range(N)]
# tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
# mpld3.plugins.connect(fig, tooltip)

# mpld3.show()

# html = mpld3.fig_to_html(fig)
mpld3.save_html(fig, 'test1.html')
# print html


def make_donut(sizes, text, colors, labels):
	col = [[i / 255 for i in c] for c in colors]

	fig, ax = plt.subplots()
	ax.axis('equal')
	width = 0.35
	# width = 0.75
	kwargs = dict(colors=col, startangle=180)
	outside = ax.pie(sizes, radius=1, pctdistance=1-width/2, autopct='%1.1f%%', labels=labels, **kwargs)[0]
	plt.setp(outside, width=width, edgecolor='white')

	kwargs = dict(size=20, fontweight='bold', va='center')
	ax.text(0, 0, text, ha='center', **kwargs)
	# plt.show()
	mpld3.save_html(fig, 'test2.html')


# c1 = (226, 33, 7)
c1 = (80, 80, 80)
c2 = (60, 121, 189)

make_donut([5, 95], "Test", [c1, c2], ['Free', 'Load'])
