import re
import requests
from bs4 import BeautifulSoup
from getpass import getpass

#Adjust URL
site = input("Enter a url:\n")

folder = input("Enter a output folder:\n")

user = input("Enter a user:\n")

password = getpass("password: ")

response = requests.get(site, auth=(user, password))

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]

for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    newfile = folder + filename.group(1)
    with open(newfile, 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)