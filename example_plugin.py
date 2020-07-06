# -*- coding: utf-8 -*-

cool_qq_api = None


def on_qq_load(server, bot):
    server.logger.info('calling on_qq_load')
    bot.send_msg('QQ bot example plugin is starting up', group_id=1234567)


def on_qq_info(server, info, bot):
    server.logger.info('calling on_qq_info')
    if info.raw_content == 'say hi!':
        server.say('hi! I am the qq bot.')


def on_qq_command(server, info, bot):
    server.logger.info('calling on_qq_command')
    if info.content == ('/stop'):
        server.stop()
    server.logger.error(info.content)


def on_qq_notice(server, info, bot):
    server.logger.info('calling on_qq_notice')


def on_load(server, old_module):
    global cool_qq_api
    cool_qq_api = server.get_plugin_instance('CoolQQAPI-MCDR')


def on_info(server, info):
    if info.content.startswith('!!qq send '):
        cool_qq_api.get_bot().send_msg(info.content[10:], group_id=1234567)
