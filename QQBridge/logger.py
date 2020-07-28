# -*- coding: utf-8 -*-
import logging
import time
import os
import zipfile


class Logger:
    fmt = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def __init__(self):
        logging.getLogger('werkzeug').setLevel(logging.ERROR)
        self.file_path = 'logs/log.log'
        if not os.path.isdir('logs'):
            os.mkdir('logs')
        self.set_file()
        self.logger = logging.getLogger('QQBridge')
        self.logger.setLevel(logging.INFO)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)
        self.ch.setFormatter(self.fmt)
        self.logger.addHandler(self.ch)
        self.fh = logging.FileHandler(self.file_path, encoding='utf-8')
        self.fh.setLevel(logging.INFO)
        self.fh.setFormatter(self.fmt)
        self.logger.addHandler(self.fh)

        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.critical = self.logger.critical
        self.exception = self.logger.exception

    def set_file(self):
        try:
            self.logger.removeHandler(self.fh)
        except AttributeError:
            pass
        if os.path.isfile(self.file_path):
            modify_time = time.strftime('%Y-%m-%d', time.localtime(
                os.stat(self.file_path).st_mtime))
            counter = 0
            while True:
                counter += 1
                zip_file_name = 'logs/{}-{}.zip'.format(modify_time, counter)
                if not os.path.isfile(zip_file_name):
                    break
            zipf = zipfile.ZipFile(zip_file_name, 'w')
            zipf.write(self.file_path, arcname=os.path.basename(self.file_path),
                       compress_type=zipfile.ZIP_DEFLATED)
            zipf.close()
            os.remove(self.file_path)
