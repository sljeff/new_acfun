#!/usr/bin/env python3
# coding: utf-8
import os
import requests
import gevent
from gevent import monkey
monkey.patch_all()

numbers = [str(i) if i > 9 else '0'+str(i) for i in range(1, 56)]
url = 'http://cdn.aixifan.com/dotnet/20130418/umeditor/dialogs/emotion/images/ac2/{}.gif'
urls = [url.format(x) for x in numbers]

if not os.path.isdir('img'):
    os.mkdir('img')


def download_img(img_url, save_path='img'):
    """
    :type img_url: str
    """
    try:
        r = requests.get(img_url, timeout=5)
    except TimeoutError:
        try:
            r = requests.get(img_url, timeout=5)
        except TimeoutError:
            return False
    save_name = img_url.split('/')[-1]
    with open(os.path.join(save_path, save_name), 'wb') as f:
        f.write(r.content)
    return True

jobs = [gevent.spawn(download_img, url) for url in urls]
gevent.joinall(jobs)

import pprint
pprint.pprint([job.value for job in jobs])
