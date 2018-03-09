import urllib.request

username = ''
link = r'https://www.instagram.com/' + username
html = urllib.request.urlopen(link)
print(html.read())