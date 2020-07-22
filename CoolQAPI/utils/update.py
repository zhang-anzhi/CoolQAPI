# -*- coding: utf-8 -*-
import requests
import os
from threading import Thread
from .constant import VERSION, NAME

url = 'https://api.github.com/repos/zhang-anzhi/CoolQAPI/releases/latest'


def check(server):
    t = Thread(target=check_update, args=(server,), name='CoolQAPI Updater')
    t.start()


def check_update(server):
    server.logger.info('检测更新中')
    r = requests.get(url).json()
    compare = version_compare(r['tag_name'][1:], VERSION)
    if compare == 0:
        server.logger.info('CoolQAPI 已为最新版')
    elif compare == 1:
        download_link = r['assets'][0]['browser_download_url']
        server.logger.info('检测到新版本: ' + r['tag_name'][1:])
        download(server, download_link, r['tag_name'][1:])


def download(server, download_link, ver):
    update_path = '.\\plugins\\CoolQAPI\\CoolQAPI_update'
    if not os.path.isdir(update_path):
        os.mkdir(update_path)
    with open(f'{update_path}\\{NAME}-{ver}.zip', 'wb') as f:
        f.write(requests.get(download_link).content)
    server.logger.info(f'更新下载完成, 文件位于{update_path[2:]}\\{NAME}-{ver}.zip')


def version_compare(v1, v2):
    """by Fallen_Breath"""

    def split_version(v):
        return tuple([int(x) for x in v.split('-')[0].split('.')])

    def cmp(a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    v1 = split_version(v1)
    v2 = split_version(v2)
    for i in range(min(len(v1), len(v2))):
        if v1[i] != v2[i]:
            return cmp(v1[i], v2[i])
    else:
        return cmp(len(v1), len(v2))
