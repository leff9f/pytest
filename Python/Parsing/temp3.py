import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        }

url = "https://www.phoenixcontact.com/assets/images_pr/product_photos/large/25176_1000_int_04.jpg"
response = requests.get(url, headers=headers)
if response.status_code == 200:
    with open(".sample.jpg", 'wb') as f:
        f.write(response.content)


