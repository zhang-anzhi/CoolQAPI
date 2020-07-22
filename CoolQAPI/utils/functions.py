# -*- coding: utf-8 -*-

import sys
import importlib.util


def load_source(path, name=None):
    if name is None:
        name = path.replace('plugins/', '').replace('plugins\\', '')
        name = name.replace('/', '_').replace('\\', '_')[:-3]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def version_compare(v1, v2):
    """by Fallen_Breath"""

    def split_version(v):
        return tuple([int(x) for x in v.split('-')[0].split('.')])

    def cmp(a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    v1 = split_version(v1)
    v2 = split_version(v2)
    for i in range(min(len(v1), len(v2))):
        if v1[i] != v2[i]:
            return cmp(v1[i], v2[i])
    else:
        return cmp(len(v1), len(v2))
