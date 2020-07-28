# -*- coding: utf-8 -*-

import json
import logging
from threading import Thread
from flask import Flask, request

from .info import Info


class PostServer(Thread):
    def __init__(self, config):
        super().__init__(name='CoolQAPI server')
        self.bot_server = Flask(__name__)
        self.server = None
        self.info = None
        self.config = config
        logging.getLogger('werkzeug').setLevel(logging.ERROR)

    def init(self, server, config):
        self.server = server
        self.config = config
        self.info = Info(self.server, self.config)

        @self.bot_server.route('/post', methods=['POST'])
        def server():
            self.info.parse(json.loads(request.get_data().decode('utf-8')))
            return ''

    def run(self):
        self.server.logger.info('CoolQAPI server is starting up')
        self.bot_server.run(port=self.config['post_port'],
                            host=self.config['post_host'],
                            threaded=False)
        self.server.logger.info('CoolQAPI server was exit')

    def load_event(self):
        """load plugins"""
        self.info.load_event()

    def get_bot(self):
        """get bot object"""
        return self.info.get_bot()
