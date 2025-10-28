# -*- coding: utf-8 -*-
import sys

try:
    from importlib import resources

    get_module_res = lambda f: str(resources.files("jieba").joinpath(f))
except ImportError:
    import importlib_resources

    get_module_res = lambda f: str(importlib_resources.files("jieba").joinpath(f))

default_encoding = sys.getfilesystemencoding()


text_type = str
string_types = (str,)
xrange = range

iterkeys = lambda d: iter(d.keys())
itervalues = lambda d: iter(d.values())
iteritems = lambda d: iter(d.items())


def strdecode(sentence):
    if not isinstance(sentence, text_type):
        try:
            sentence = sentence.decode("utf-8")
        except UnicodeDecodeError:
            sentence = sentence.decode("gbk", "ignore")
    return sentence


def resolve_filename(f):
    try:
        return f.name
    except AttributeError:
        return repr(f)
