# -*- coding: utf-8 -*-

import json
import re
from flask import request

from .bot import Bot
from .event import Event


class Info:
    def __init__(self, server, config):
        self.__data = None
        self.__func = None
        self.config = config
        self.__server = server
        self.__bot = Bot(self.config)
        self.__event = Event(self.__server, self.__bot)

        # parse
        # global
        self.raw = None
        self.time = None
        self.post_type = None
        self.source_type = None
        self.source_id = None

        # message
        self.message_id = None
        self.user_id = None
        self.source_sub_type = None
        self.raw_content = None
        self.content = None

        # notice
        self.notice_type = None

        # group_ban
        self.duration = None
        self.operator_id = None
        self.notice_sub_type = None

        # group_upload
        self.file_busid = None
        self.file_id = None
        self.file_name = None
        self.file_size = None

    def init_parser(self):
        # global
        self.raw = None
        self.time = None
        self.post_type = None
        self.source_type = None
        self.source_id = None

        # message
        self.message_id = None
        self.user_id = None
        self.source_sub_type = None
        self.raw_content = None
        self.content = None

        # notice
        self.notice_type = None

        # group_ban
        self.duration = None
        self.operator_id = None
        self.notice_sub_type = None

        # group_upload
        self.file_busid = None
        self.file_id = None
        self.file_name = None
        self.file_size = None

    def parse(self, data):
        """base parser"""
        # dict
        self.__data = data

        # TODO: remove debug
        # self.__server.logger.warning(
            # json.dumps(self.__data, indent=4, ensure_ascii=False))

        # shutdown:
        if 'shutdown' in self.__data.keys() and self.__data['shutdown'] is True:
            return self.__shutdown()

        # global
        self.init_parser()
        self.raw = self.__data
        self.time = self.__data['time']
        self.post_type = self.__data['post_type']

        # 两种类型的上报
        if self.post_type == 'message':
            self.message_parse()
        elif self.post_type == 'notice':
            self.notice_parse()

    def message_parse(self):
        self.message_id = self.__data['message_id']
        self.user_id = self.__data['user_id']
        self.source_type = self.__data['message_type']
        self.source_sub_type = self.__data['sub_type']
        self.raw_content = self.__data['message']
        self.content_parse()
        if self.source_type == 'private':
            self.source_id = self.__data['user_id']
        elif self.source_type == 'group':
            self.source_id = self.__data['group_id']

        # call on_qq_info
        self.__event.call('on_qq_info', (self.__server, self, self.__bot))
        # call on_qq_command
        if self.content.startswith(self.config['command_prefix']):
            self.__event.call('on_qq_command', (self.__server, self, self.__bot))

    def notice_parse(self):
        self.notice_type = self.__data['notice_type']
        # group_ban
        if self.notice_type == 'group_ban':
            self.source_type = 'group'
            self.source_id = self.__data['group_id']
            self.user_id = self.__data['user_id']
            self.duration = self.__data['duration']
            self.operator_id = self.__data['operator_id']
            self.notice_sub_type = self.__data['sub_type']

        # group_upload
        elif self.notice_type == 'group_upload':
            self.source_type = 'group'
            self.source_id = self.__data['group_id']
            self.user_id = self.__data['user_id']
            self.file_busid = self.__data['file']['busid']
            self.file_id = self.__data['file']['id']
            self.file_name = self.__data['file']['name']
            self.file_size = self.__data['file']['size']

        # call on_qq_notice
        self.__event.call('on_qq_notice', (self.__server, self, self.__bot))

    def content_parse(self):
        content = self.__data['raw_message']
        content = re.sub(r'\[CQ:image,file=.*?\]', '[图片]', content)
        content = re.sub(r'\[CQ:share,file=.*?\]', '[链接]', content)
        content = re.sub(r'\[CQ:face,file=.*?\]', '[表情]', content)
        content = re.sub(r'\[CQ:record,file=.*?\]', '[语音]', content)
        content = content.replace('CQ:at,qq=', '@')
        self.content = content

    def __shutdown(self):
        self.__func = request.environ.get('werkzeug.server.shutdown')
        if self.__func is None:
            raise RuntimeError
        self.__func()

    def __getitem__(self, item):
        return self.raw[item]

    def load_event(self):
        """load plugins"""
        self.__event.load()

    def get_bot(self):
        """get bot object"""
        return self.__bot
