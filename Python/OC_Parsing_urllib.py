import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        }


url = 'https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid=1205448&library=ruru&pcck=P-10-01-03&tab=1&selectedCategory=ALL'
r = requests.get(url, headers=headers)

log = open('test.html', 'w', encoding='utf-8')
print(r.text, file=log)