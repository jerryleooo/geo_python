# -*- coding: utf-8 -*-

from redis import StrictRedis
from .exc import InvalidPointError


default_config = {
    'GEO_DEFAULT_HOST': 'localhost',
    'GEO_DEFAULT_PORT': 6379,
    'GEO_DEFAULT_PASSWORD': None,
    'GEO_DEFAULT_DB': 0
}


class MetaPoint(type):

    def __new__(cls, name, bases, attrs):
        if name != 'Point' and '__key__' not in attrs:
            raise InvalidPointError("__key__ should be specified")
        cls.redis_store = cls.read_config()
        return type.__new__(cls, name, bases, attrs)

    @classmethod
    def read_config(cls):

        if 'config' not in cls.__dict__:
            config = default_config
        else:
            config = cls.config

        return StrictRedis(host=config['GEO_DEFAULT_HOST'],
                           port=config['GEO_DEFAULT_PORT'],
                           password=config['GEO_DEFAULT_PASSWORD'],
                           db=config['GEO_DEFAULT_DB'])


class Point(object):

    __metaclass__ = MetaPoint

    def __init__(self, longitude, latitude, member):
        self.longitude = longitude
        self.latitude = latitude
        self.member = member

    @classmethod
    def create(cls, longitude, latitude, member):
        cls.redis_store.geoadd(cls.__key__, longitude, latitude, member)
        return cls(longitude, latitude, member)

    def delete(cls):
        pass

    def update(self):
        pass

    def query_by_pos(self, longitude, latitude):
        pass

    def geo_hash(self):
        return self.redis_store.geohash(self.member)

