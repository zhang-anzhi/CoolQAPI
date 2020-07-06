# -*- coding: utf-8 -*-

import sys
import importlib.util


def load_source(path, name=None):
    if name is None:
        name = path.replace('/', '_').replace('\\', '_')[:-3]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module
