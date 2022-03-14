
#! /usr/bin/env python3

import os
import requests

dir = "/data/feedback"

for file in os.listdir(dir):
    format = ['title','name','date','feedback']

    content = {}
    with open('{}/{}'.format(dir,file), 'r') as txtfile:
        i = 0
        for line in txtfile:
            line = line.replace("\n", "")
            content[format[i]] = line.strip('\n')
            i += 1
    response = requests.post('http://34.132.189.7/feedback/', json = content)

    if not response.ok:
        raise Exception('POST failed! | Status code: {} | File: {}'.format(resp$
    print('Feedback added!')
