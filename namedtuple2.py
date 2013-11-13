#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['namedtuple2']

class namedtuple2(tuple):
    """A minimal implementation of tuple with named fields.

    It works well if you just get fields by names, but you **OUGHT NOT TO** modify (set or delete)
    instance-level or class-level attributes of `namedtuple2`.

        >>> names = ('x', 'y')
        >>> values = (1, 2)
        >>> p = namedtuple2(names, *values)
        >>> p
        namedtuple2(x=1, y=2)
        >>> p.x, p.y
        (1, 2)
        >>> p[0], p[1]
        (1, 2)

        >>> from functools import partial
        >>> point = partial(namedtuple2, ('x', 'y'))
        >>> point(1, 2)
        namedtuple2(x=1, y=2)
    """
    def __new__(cls, names, *values):
        assert (len(names) == len(values)), \
               'length of {!r} and {!r} must be equal'.format(names, values)
        map(assertname, names)

        inst = super(namedtuple2, cls).__new__(cls, values)
        inst._fields = tuple(names)
        for i, name in enumerate(names):
            inst.__dict__[name] = inst[i]
        return inst

    def __repr__(self):
        paras = ['%s=%r' % (name, self[i]) for i, name in enumerate(self._fields)]
        return 'namedtuple2(%s)' % ', '.join(paras)

def assertname(name):
    if not (name and isinstance(name, str)):
        raise ValueError('Field names must be non-empty string')
    if not all(c.isalnum() or c=='_' for c in name):
        raise ValueError('Field names can only contain '
                         'alphanumeric characters and underscores: %r' % name)
    if name[0].isdigit():
        raise ValueError('Field names cannot start with '
                         'a number: %r' % name)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
