simplehtml
============================

.. image:: https://img.shields.io/pypi/v/simplehtml.svg
	:target: https://pypi.python.org/pypi/simplehtml/
	:alt: Latest Version
.. image:: https://img.shields.io/pypi/l/simplehtml.svg
	:target: https://pypi.python.org/pypi/simplehtml/
	:alt: License
.. image:: https://travis-ci.org/walchko/simplehtml.svg?branch=master
	:target: https://travis-ci.org/walchko/simplehtml
.. image:: https://api.codacy.com/project/badge/Grade/af6dc70daea843dc8d48c190a0076ccb
	:target: https://www.codacy.com/app/kevin-walchko/simplehtml?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=walchko/simplehtml&amp;utm_campaign=Badge_Grade

A light weight html library to create web pages dynamically. This is used in
some of my embedded applications to save me from reinventing the wheel over and
over.

Install
-----------

pip
~~~~~

::

	pip install simplehtml

Development
~~~~~~~~~~~~~

::

	git clone https://github.com/walchko/simplehtml
	cd simplehtml
	pip install -e .

Usage
---------

To build a webpage with a simple table on it, do:

.. code-block:: python

	from simplehtml import HTML, CSS

	# make a simple table
	data = {
		"header": [5, 6, 7],  # optional table header
		"data": [
			["hello", "hi", "ola"],
			[1, 2, 3],
			["a", "b", "c"]
		]
	}

	html = HTML()
	html.css(CSS.cssTable())  # make the table look pretty
	html.h1('My awesome table')
	html.table(data)
	print html

To just create a simple webpage, you can just call standard tags like ``h1``,
``h2``, ``img``, etc and create a page. Note, only a small (common?) selection
of tags is supported.

.. code-block:: python

	from simplehtml import HTML

	# create your own css
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
	html.p('this is a paragraph')
	html.p('this is another paragraph')
	html.footer('<a href="https://github.com/walchko">my code</a>')
	print html

Change Log
-------------

========== ======= =============================
2016-12-20 0.2.0   better table support and cleanup
2016-12-14 0.0.1   init
========== ======= =============================

License
-----------

**The MIT License (MIT)**

Copyright (c) 2016 Kevin J. Walchko

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
