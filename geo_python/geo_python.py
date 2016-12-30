# -*- coding: utf-8 -*-

from redis import StrictRedis

class Point(object):

    def __init__(self, longitude, latitude, member):
        pass

    @classmethod
    def add(cls, longitude, latitude, member):
        # redis.geoadd(self.__key__, longitude, latitude, member)
        return cls(longitude, latitude, member)
