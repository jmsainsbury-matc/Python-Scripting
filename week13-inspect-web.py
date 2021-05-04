#!/usr/bin/env python3
import requests, bs4

res = requests.get('https://notpurple.com')

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
title = soup.select('title')

links = soup.select('a')


print(title)
print(links)

