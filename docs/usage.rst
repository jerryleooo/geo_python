=====
Usage
=====

To use GEO Python in a project::

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
