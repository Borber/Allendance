# -*- coding: utf-8 -*-
import random

import requests,os

heards = {
        'Host': 'www.v2ex.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Referer': 'https://www.v2ex.com/mission/daily',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
}
cookies = {}
def init(cookie):
    c = cookie
    for line in c.split(';'):
    #其设置为1就会把字符串拆分成2份
        name,value=line.strip().split('=',1)
        cookies[name]=value

def main(Cookie):
    init(Cookie)
    r = requests.Session()
    getHash = r.get(url='https://www.v2ex.com/mission/daily/redeem?once=23077',headers=heards,cookies= cookies)
    print(getHash.text)


if __name__ == '__main__':
    main(os.environ['VVEX'])




