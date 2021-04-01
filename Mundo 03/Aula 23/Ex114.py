import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site não está disponível!\033[m')
else:
    print('\033[32mO site está disponível!\033[m')
