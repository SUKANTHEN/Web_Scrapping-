# Scrapping an image data using request library

import requests
r = requests.get('path/to/forest.jpg', stream=True)
r.raise_for_status()
with open('Mountain.jpg', 'wb') as file:
for chunk in r.iter_content(chunk_size=50000):
file.write(chunk)
