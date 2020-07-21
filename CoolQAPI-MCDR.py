# -*- coding: utf-8 -*-

import time

from plugins.CoolQAPI.utils.functions import load_source

cool_q_api = load_source('plugins/CoolQAPI/CoolQAPI.py')

help_msg = '''
§6!!CQ reload all §7重载所有
§6!!CQ reload plugin §7重载插件'''


def on_load(server, old):
    time.sleep(1)
    global cool_q_api
    try:
        if old is not None and old.cool_q_api is not None:
            cool_q_api = old.cool_q_api
        else:
            start(server)
    except:
        start(server)


def on_mcdr_stop(server):
    server.logger.info('Waiting for CoolQAPI server stop')
    stop()


def start(server):
    global cool_q_api
    cool_q_api = load_source('plugins/CoolQAPI/CoolQAPI.py')
    cool_q_api.start(server)


def stop():
    global cool_q_api
    cool_q_api.stop()


def on_user_info(server, info):
    if info.content == '!!CQ':
        server.reply(info, help_msg)
    elif info.content.startswith('!!CQ '):
        command(server, info, info.content.split(' '))


def command(server, info, command):
    if len(command) == 3 and command[1] == 'reload':
        if command[2] == 'all':
            stop()
            time.sleep(1)
            start(server)
            time.sleep(0.1)
            server.reply(info, '§a已成功重载所有')
        elif command[2] == 'plugin':
            reload_plugins()
            server.reply(info, '§a已成功重载插件')
    else:
        server.reply(info, '§c未知指令')


def reload_plugins():
    """reload plugins api"""
    global cool_q_api
    cool_q_api.load_event()


def get_bot():
    """return bot object"""
    global cool_q_api
    return cool_q_api.get_bot()
