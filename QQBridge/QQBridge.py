# -*- coding: utf-8 -*-
import requests
import json
from flask import Flask, request
from config import Config
from logger import Logger

config = {}


class QQBridge:
    def __init__(self):
        self.logger = Logger()
        self.config = Config('config.yml')
        self.server = Flask(__name__)
        self.start()
        self.logger.info(f'接收服务器以地址 {self.config["post_host"]}:'
                         f'{self.config["post_port"]}'
                         f'{self.config["post_url"]} 启动中')
        self.server.run(port=self.config['post_port'],
                        host=self.config['post_host'],
                        threaded=False)

    def start(self):
        @self.server.route(self.config['post_url'], methods=['POST'])
        def recv():
            data = json.loads(request.get_data().decode('utf-8'))
            self.logger.info('接收到数据')
            self.logger.info(json.dumps(data, indent=4, ensure_ascii=False))
            self.send(data)
            return ''

    def send(self, data):
        for i in self.config['server_list']:
            target = f'http://{self.config["post_host"]}:{i}/post'
            try:
                requests.post(target, json=data)
                self.logger.info('将数据转发到' + target)
            except:
                self.logger.info(f'转发到{target}失败')


bridge = QQBridge()
