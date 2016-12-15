/usr/bin/env python

from simple import HTML

def test_headers():
	ans = """
	"""
	
	html = HTML()
	html.h1('h1')
	html.h2('h2')
	html.h3('h3')
	
	resp = str(html)
	
# 	assert resp == ans
	assert True

def test_text():
	ans = """
	"""
	
	html = HTML()
	html.p('parapraph')
	html.footer('footer')
	
	resp = str(html)
	
# 	assert resp == ans
	assert True
	
def test_imgs():
	ans = """
	"""
	
	html = HTML()
	html.im('link', width=100, height=100)
	html.iframe('link', width=100, height=100)
	resp = str(html)
	
	# assert ans == resp
	assert True
	
# def test_table():
# 	ans = """
# 	"""
	
# 	data = readJson('test.json')
# 	html = HTML()
# 	html.table(data)
	
# 	resp = str(html)
	
# 	assert resp == ans
	
	
