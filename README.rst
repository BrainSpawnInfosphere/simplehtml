simplehtml
============================

.. image:: https://img.shields.io/pypi/v/simplehtml.svg
	:target: https://pypi.python.org/pypi/simplehtml/
	:alt: Latest Version
.. image:: https://img.shields.io/pypi/l/simplehtml.svg
	:target: https://pypi.python.org/pypi/simplehtml/
	:alt: License

A light weight html library to create web pages dynamically.

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

If you want to use some of the classes and functions:

.. code-block:: python

	from simplehtml import HTML, readJson

	html = HTML()
	html.p('hi')

	data = readJson('myfile.json')

.. code-block:: python

	from simplehtml import HTML

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
	html.p('this is another paragraph')
	html.footer('<a href="https://github.com/walchko">my code</a>')
	print html

Change Log
-------------

========== ======= =============================
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
