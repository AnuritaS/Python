#!/usr/bin/env python
import sys
import cgi
print('Content-type: text/html\r\n\r\n')
print('<html>')
print('<table border=1>')
form = cgi.FieldStorage()
w = form['first'].value
w1 = form['second'].value
print('<tr>')
print('<th>Authorname</th>')
print('<th>BOOKNAME</th>')
print('</tr>')
print('<tr>')
print('<td>%s</td>'%(w))
print('<td>%s</td>'%(w1))
print('</tr>')
print('</table>')
print('</html>')
text = """Content-type: text/html\r\n\r\n
<html>
<body>
<form action="file.py" method="post">
  AuthorNmae:<br>
  <input type="text" name="first"><br>
  BookNmae:<br>
  <input type="text" name="second"><br>
  <input type="submit" value="send" name="button">
 </form>

<body>
</html>"""
print(text)

'''#!/usr/bin/env python3.4'''
from http.server import HTTPServer, CGIHTTPRequestHandler

srv = HTTPServer(('', 80), CGIHTTPRequestHandler)
srv.serve_forever()