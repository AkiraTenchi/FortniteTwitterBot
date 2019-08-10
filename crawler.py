import requests
from bs4 import BeautifulSoup as bs
import os

# website with model images
url = 'https://wall.alphacoders.com/by_sub_category.php?id=192890&name=Fortnite+Wallpapers'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')


print(len(image_tags))
print(image_tags)

# create directory for model images
if not os.path.exists('models'):
    os.makedirs('models')

# move to new directory
os.chdir('models')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        print(image['alt'])
        if "Wallpaper" in image['alt']:
            url = image['data-src']
            response = requests.get(url)
            if response.status_code == 200:
                with open('model-' + str(x) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    f.close()
                    x += 1
    except:
        pass