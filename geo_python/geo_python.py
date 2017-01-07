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

    def delete(self):
        return self.__class__.redis_store.zrem(self.__key__, self.member)

    def update(self, **kwargs):
        self.longitude = kwargs.get("longitude") or self.longitude
        self.latitude = kwargs.get("latitude") or self.latitude
        self.member = kwargs.get("member") or self.member

    @classmethod
    def get_by_member(cls, member):
        longitude, latitude = cls.redis_store.geopos(cls.__key__, member)[0]
        return cls(longitude, latitude, member)

    @classmethod
    def query_by_pos(cls, longitude, latitude, dist=100, unit='m'):
        member_list = cls.redis_store.georadius(cls.__key__, longitude, latitude, dist, unit)
        return [cls.get_by_member(member) for member in member_list]

    @classmethod
    def query_by_member(cls, member, dist=100, unit='m'):
        member_list = cls.redis_store.georadiusbymember(cls.__key__, member, dist, unit)
        return [cls.get_by_member(_member) for _member in member_list]

    @classmethod
    def dist(cls, point1, point2):
        return cls.redis_store.geodist(cls.__key__, point1.member, point2.member)

    def geo_hash(self):
        return self.__class__.redis_store.geohash(self.__key__, self.member)

    def __str__(self):
        return '<%s __key__:%s longitude:%s latitude:%s member:%s>' % \
               (self.__class__.__name__, self.__key__, self.longitude, self.latitude, self.member)

    __repr__ = __str__
