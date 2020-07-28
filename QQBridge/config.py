# -*- coding: utf-8 -*-
import os
import yaml


class Config:
    def __init__(self, file_path):
        self.data = None
        self.file_path = file_path
        if os.path.isfile(self.file_path):
            with open(self.file_path, encoding='utf8') as file:
                self.data = yaml.safe_load(file)
        self.check_config()

    def touch(self, key, default):
        if self.data is None:
            self.data = {}
        if key not in self.data:
            self.data[key] = default
            with open(self.file_path, 'a', encoding='utf8') as file:
                yaml.safe_dump({key: default}, file)

    def check_config(self):
        self.touch('post_host', '127.0.0.1')
        self.touch('post_port', 5701)
        self.touch('post_url', '/post')
        self.touch('server_list', [])

    def __getitem__(self, item):
        return self.data[item]
