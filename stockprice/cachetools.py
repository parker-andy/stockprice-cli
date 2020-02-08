from collections import namedtuple
import json
import os
from . import validation
from .cache import JsonFileCache


class Folder(object):
    CHART = 'chart'
    SUMMARY = 'summary'


Document = namedtuple('Document', ('filename', 'contents'))


class DocumentStore(object):
    def __init__(self, path):
        self._path = path

    @classmethod
    def from_path_segments(cls, *segments):
        path = os.path.join(*segments)
        return cls(path)

    def documents(self):
        filenames = os.listdir(self._path)
        for filename in filenames:
            fullpath = os.path.join(self._path, filename)
            with open(fullpath) as f:
                yield Document(filename=filename, contents=json.load(f))

    def get_or_create(self, name, factory, **kwargs):
        if not validation.is_valid_filename(name):
            raise ValueError(f'Cannot create document for name "{name}"')
        full_path = os.path.join(self._path, '.'.join((name, 'json')))
        return JsonFileCache(full_path, **kwargs).get_values(factory)
