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
	# assert True


def test_text():
	# ans = '<!DOCTYPE html><html><head><style></style></head><body><p>paragraph</p><footer>footer</footer></body></html>'
	ans = '<!DOCTYPE html><html><head><style></style></head><body><p>parapraph</p><footer>footer</footer></body></html>'
	html = HTML()
	html.p('parapraph')
	html.footer('footer')

	resp = str(html)
	# print('resp', resp)
	# print('ans', ans)
	# print(ans==resp)
	# print(ans==ans2)

	assert resp == ans
	# assert True


def test_imgs():
	ans = '<!DOCTYPE html><html><head><style></style></head><body><img src="link" alt="img" width="100" height="100"><iframe src="link" alt="img" width="100" height="100"></body></html>'

	html = HTML()
	html.img('link', width=100, height=100)
	html.iframe('link', width=100, height=100)
	resp = str(html)
	# print('resp', resp)
	# print('ans', ans)
	# print(ans==resp)

	assert ans == resp
	# assert True

# def test_table():
# 	ans = """
# 	"""

# 	data = readJson('test.json')
# 	html = HTML()
# 	html.table(data)

# 	resp = str(html)

# 	assert resp == ans
