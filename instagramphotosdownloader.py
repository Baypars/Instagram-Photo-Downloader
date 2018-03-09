import urllib.request

link = r'https://www.instagram.com/justmegawatt/'
html = urllib.request.urlopen(link)
print(html.read())