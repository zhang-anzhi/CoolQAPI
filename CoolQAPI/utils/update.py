# -*- coding: utf-8 -*-
import requests
import os
from threading import Thread
from .constant import VERSION, NAME
from .functions import version_compare

url = 'https://api.github.com/repos/zhang-anzhi/CoolQAPI/releases/latest'


def check(server):
    t = Thread(target=check_update, args=(server,), name='CoolQAPI Updater')
    t.start()


def check_update(server):
    try:
        server.logger.info('检查更新中')
        r = requests.get(url).json()
        try:
            compare = version_compare(r['tag_name'], VERSION)
        except ValueError:
            server.logger.error('您的版本号错误, 自动为您下载最新版中')
            compare = 1
        if compare == 0:
            server.logger.info('CoolQAPI 已为最新版')
        elif compare == 1:
            server.logger.info('发现新版本: ' + r['tag_name'])
            download_link = r['assets'][0]['browser_download_url']
            download(server, download_link, r['tag_name'])
        elif compare == -1:
            server.logger.info('检测到 CoolQAPI 为开发版')
    except requests.exceptions.ProxyError:
        server.logger.error('CoolQAPI 更新失败')


def download(server, download_link, ver):
    update_path = '.\\plugins\\CoolQAPI\\CoolQAPI_update'
    if not os.path.isdir(update_path):
        os.mkdir(update_path)
    with open(f'{update_path}\\{NAME}-{ver}.zip', 'wb') as f:
        f.write(requests.get(download_link).content)
    server.logger.info(f'更新下载完成, 文件位于{update_path[2:]}\\{NAME}-{ver}.zip')
