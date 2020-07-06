# -*- coding: utf-8 -*-
import os
import yaml


class Config:
    def __init__(self, file_name):
        self.data = None
        self.file_name = file_name
        if os.path.isfile(self.file_name):
            with open(self.file_name, encoding='utf8') as file:
                self.data = yaml.safe_load(file)
        self.check_config()

    def save(self):
        with open(self.file_name, 'w', encoding='utf8') as file:
            yaml.safe_dump(self.data, file)

    def touch(self, key, default):
        if self.data is None:
            self.data = {}
        if key not in self.data:
            self.data[key] = default
            with open(self.file_name, 'a', encoding='utf8') as file:
                yaml.safe_dump({key: default}, file)

    def check_config(self):
        self.touch('post_host', '127.0.0.1')
        self.touch('post_port', 5701)
        self.touch('post_url', '/post')
        self.touch('api_host', '127.0.0.1')
        self.touch('api_port', 5700)
        self.touch('command_prefix', '/')

    def __getitem__(self, item):
        return self.data[item]
