# -*- coding: utf-8 -*-

import os
from threading import Thread

from .functions import *


class Event:
    def __init__(self, server, bot):
        self.__server = server
        self.__bot = bot

        self.plugin_list = []
        self.file_list = os.listdir('./plugins')
        self.load()

    def load(self):
        self.plugin_list = []
        self.file_list = os.listdir('./plugins')
        for i in self.file_list:
            if i.endswith('.py'):
                self.plugin_list.append(load_source('plugins/' + i))
        self.call('on_qq_load', (self.__server, self.__bot))

    def call(self, func_name, args=()):
        for plugin in self.plugin_list:
            if hasattr(plugin, func_name):
                target = plugin.__dict__[func_name]
                if callable(target):
                    thread = PluginThread(target, args, plugin, func_name)
                    thread.start()


class PluginThread(Thread):
    def __init__(self, target, args, plugin, func_name):
        super().__init__(target=target, args=args,
                         name=f'{func_name}@{plugin.__name__[8:]}')

    def run(self):
        try:
            super().run()
        except:
            pass
