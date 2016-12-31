# -*- coding: utf-8 -*-

from redis import StrictRedis
from .exc import InvalidPointError


redis_store = StrictRedis(host='localhost', port='6379', db=0)

default_config = {
    'GEO_DEFAULT_HOST': 'localhost',
    'GEO_DEFAULT_PORT': 6379,
    'GEO_DEFAULT_PASSWORD': None,
    'GEO_DEFAULT_DB': 0
}


def read_config(config=None):
    if not config:
        config = default_config

    return StrictRedis(host=config['GEO_DEFAULT_HOST'],
                       port=config['GEO_DEFAULT_PORT'],
                       password=config['GEO_DEFAULT_PASSWORD'],
                       db=config['GEO_DEFAULT_DB'])

class Point(object):

    redis_store = read_config()

    def __init__(self, longitude, latitude, member):
        if not hasattr(self, '__key__'):
            raise InvalidPointError("__key__ should be defined in Point subclass")

        self.longitude = longitude
        self.latitude = latitude
        self.member = member

    @classmethod
    def add(cls, longitude, latitude, member):
        redis_store.geoadd(cls.__key__, longitude, latitude, member)
        return cls(longitude, latitude, member)
