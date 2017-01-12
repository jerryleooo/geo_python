# -*- coding: utf-8 -*-

from redis import StrictRedis
from .exc import InvalidPointError


default_config = {
    'GEO_REDIS_HOST': 'localhost',
    'GEO_REDIS_PORT': 6379,
    'GEO_REDIS_PASSWORD': None,
    'GEO_REDIS_DB': 0
}


class MetaPoint(type):
    """The metaclass of Point"""

    def __new__(cls, name, bases, attrs):

        """
        To declare your own Point, you must be provide the __key__
        """

        if name != 'Point' and '__key__' not in attrs:
            raise InvalidPointError("__key__ should be specified")
        cls.redis_store = cls.read_config()
        return type.__new__(cls, name, bases, attrs)

    @classmethod
    def read_config(cls):

        """
        For customized configuration, use `config`
        """

        if 'config' not in cls.__dict__:
            config = default_config
        else:
            config = cls.config

        return StrictRedis(host=config['GEO_REDIS_HOST'],
                           port=config['GEO_REDIS_PORT'],
                           password=config['GEO_REDIS_PASSWORD'],
                           db=config['GEO_REDIS_DB'])


class Point(object):

    __metaclass__ = MetaPoint

    def __init__(self, longitude, latitude, member):
        self.longitude = longitude
        self.latitude = latitude
        self.member = member

    @classmethod
    def create(cls, longitude, latitude, member):

        """
        Create a new Point instance

        Args:

            longitude(float): the point's longitude

            latitude(float): the point's latitude

            member(string): member
        """

        cls.redis_store.geoadd(cls.__key__, longitude, latitude, member)
        return cls(longitude, latitude, member)

    def delete(self):

        """
        Delete this point
        """

        return self.__class__.redis_store.zrem(self.__key__, self.member)

    def update(self, **kwargs):

        """
        Update this point

        Args:

            longitude(float): the point's longitude

            latitude(float): the point's latitude

            member(string): member
        """

        longitude = kwargs.get("longitude") or self.longitude
        latitude = kwargs.get("latitude") or self.latitude
        member = kwargs.get("member") or self.member
        self.delete()
        new_self = self.create(longitude, latitude, member)
        self.longitude = new_self.longitude
        self.latitude = new_self.latitude
        self.member = new_self.member

    @classmethod
    def get_by_member(cls, member):

        """
        Get a Point instance by its member

        Args:

            member(string): member
        """

        longitude, latitude = cls.redis_store.geopos(cls.__key__, member)[0]
        return cls(longitude, latitude, member)

    @classmethod
    def query_by_pos(cls, longitude, latitude, dist=100, unit='m'):

        """
        Query points by position

        Args:

            longitude(float): the center's longitude

            latitude(float): the center's latitude

            dist(float): the radius of the circle

            unit(string): m, km or other, the unit of the dist
        """


        member_list = cls.redis_store.georadius(cls.__key__, longitude, latitude, dist, unit)
        return [cls.get_by_member(member) for member in member_list]

    @classmethod
    def query_by_member(cls, member, dist=100, unit='m'):

        """
        Query points by member

        Args:

            member(string): the point's member

            dist(float): the radius of the circle

            unit(string): m, km or other, the unit of the dist
        """


        member_list = cls.redis_store.georadiusbymember(cls.__key__, member, dist, unit)
        return [cls.get_by_member(_member) for _member in member_list]

    @classmethod
    def dist(cls, point1, point2):

        """
        Calculate the distance between point1 and point2

        Args:

            point1(subclass of Point): a point.

            point2(subclass of Point): another point.
        """

        return cls.redis_store.geodist(cls.__key__, point1.member, point2.member)

    def geo_hash(self):

        """
        The hash of this point, can be view on http://geohash.org/<geohash-string>
        """

        return self.__class__.redis_store.geohash(self.__key__, self.member)[0]

    def __str__(self):
        return '<%s __key__:%s longitude:%s latitude:%s member:%s>' % \
               (self.__class__.__name__, self.__key__, self.longitude, self.latitude, self.member)

    __repr__ = __str__
