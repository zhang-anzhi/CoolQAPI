# -*- coding: utf-8 -*-

import os
from threading import Thread

from .functions import load_source


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
                    thread = PluginThread(
                        self.__server, target, args, plugin, func_name)
                    thread.start()


class PluginThread(Thread):
    def __init__(self, server, target, args, plugin, func_name):
        self.server = server
        self.plugin_name = plugin.__name__
        self.func_name = func_name
        super().__init__(target=target, args=args,
                         name=f'{func_name}@{self.plugin_name}')

    def run(self):
        try:
            super().run()
        except:
            self.server.logger.exception(
                f'Error calling {self.func_name} in plugin {self.plugin_name}')
