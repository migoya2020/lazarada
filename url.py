import urllib.parse
string ="lego 2514"
new = urllib.parse.quote_plus(string)
print(new)