===============================
GEO Python
===============================


.. image:: https://img.shields.io/pypi/v/geo_python.svg
        :target: https://pypi.python.org/pypi/geo_python

.. image:: https://img.shields.io/travis/jerryleooo/geo_python.svg
        :target: https://travis-ci.org/jerryleooo/geo_python

.. image:: https://readthedocs.org/projects/geo-python/badge/?version=latest
        :target: https://geo-python.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/jerryleooo/geo_python/shield.svg
     :target: https://pyup.io/repos/github/jerryleooo/geo_python/
     :alt: Updates


Simple GEO library based on Redis GEO commands

* Free software: MIT license
* Documentation: https://geo-python.readthedocs.io.


From version 3.2, Redis contains a set of very wonderful commands: the GEO commands (https://redis.io/commands#geo)

With these commands, we can easily develop LBS or GEO application.

Unfortunately, these features are not in redis-py(https://github.com/andymccurdy/redis-py) released packages, so we can only use its development version.


Get Started
-----------

::

    In [1]: from geo_python import Point
    In [2]: class MyPoint(Point):
       ...:     __key__ = 'my_point'
       ...:


    In [3]: point = MyPoint.create(120, 40, 'my point 1')
    In [4]: MyPoint.query_by_pos(point.longitude, point.latitude)
    Out[4]: [<MyPoint __key__:my_point longitude:120.000000894 latitude:39.9999999108 member:my point 1>]


    In [5]: MyPoint.query_by_member(point.member)
    Out[5]: [<MyPoint __key__:my_point longitude:120.000000894 latitude:39.9999999108 member:my point 1>]


    In [6]: point.update(member='my point 2')
    In [7]: print point.member
    my point 2

    In [8]: another_point = MyPoint.get_by_member(point.member)

    In [9]: print another_point
    <MyPoint __key__:my_point longitude:120.000000894 latitude:39.9999999108 member:my point 2>

    In [10]: print MyPoint.dist(point, another_point)
    0.0

    In [11]: point.geo_hash()
    Out[11]: 'wxj7d9v2fs0'



Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

