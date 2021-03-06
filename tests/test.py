#!/usr/bin/env python

from simplehtml import HTML


def test_headers():
	ans = '<!DOCTYPE html><html><head><style></style></head><body><h1>h1</h1><h2>h2</h2><h3>h3</h3></body></html>'

	html = HTML()
	html.h1('h1')
	html.h2('h2')
	html.h3('h3')
	resp = str(html)

	assert resp == ans


def test_text():
	ans = '<!DOCTYPE html><html><head><style></style></head><body><p>parapraph</p><footer>footer</footer></body></html>'

	html = HTML()
	html.p('parapraph')
	html.footer('footer')
	resp = str(html)

	assert resp == ans


def test_imgs():
	ans = '<!DOCTYPE html><html><head><style></style></head><body><img src="link" alt="img" width="100" height="100"><iframe src="link" alt="img" width="100" height="100"></body></html>'

	html = HTML()
	html.img('link', width=100, height=100)
	html.iframe('link', width=100, height=100)
	resp = str(html)

	assert ans == resp


def test_table():
	ans = '<!DOCTYPE html><html><head><style></style></head><body><table><tr><td>hello</td><td>hi</td><td>ola</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>a</td><td>b</td><td>c</td></tr></table></body></html>'

	info = {
		'data': [
			['hello', 'hi', 'ola'],
			[1, 2, 3],
			['a', 'b', 'c']
		]
	}

	html = HTML()
	html.table(info)
	resp = str(html)

	assert resp == ans
