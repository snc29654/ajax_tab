import cgi
import cgitb
import json
import sys
import io
import requests
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


cgitb.enable()
form=cgi.FieldStorage()
data=form.getvalue("sent")
receive=data
argv_find_all=form.getvalue("sent2")


site = requests.get(data)
data = BeautifulSoup(site.text, 'html.parser')
find_data=data.find_all(argv_find_all)




print("Content-type: text/html\n")
print(find_data)
