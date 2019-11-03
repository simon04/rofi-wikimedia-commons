#!/usr/bin/env python
'''
A rofi script to search for categories on Wikimedia Commons and copy them to clipboard.
'''
import pyperclip
import requests
import sys

search = sys.argv[1] if len(sys.argv) > 1 else ''

# copy to clipboard
if search.startswith('Category:'):
    pyperclip.copy(search)
    exit()

# search for categories on commons.wikimedia.org
print('\x00prompt\x1fSearch Wikimedia Commons categories\n')
print(f'\0message\x1fQuery: "{search}"\n')
commons = requests.get('https://commons.wikimedia.org/w/api.php', params={
    'format': 'json',
    'formatversion': '2',
    'action': 'query',
    'generator': 'search',
    'gsrnamespace': '14',
    'gsrsearch': search,
    'gsrlimit': 100,
}).json()
if 'query' not in commons or 'pages' not in commons['query']:
    exit()
for page in commons['query']['pages']:
    print(page['title'])
