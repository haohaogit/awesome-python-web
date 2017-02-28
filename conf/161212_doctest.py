import logging
import doctest
def fact(n):
    '''
    Simple dict but also support access as x.y style.

    >>> fact(4)
    24
    >>> fact(0)
    Traceback (most recent call last):
      ...
    ValueError
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6

    :param n:
    :return:
    '''
    if n<1:
        raise ValueError()
    if n==1:
        return n
    return n*fact(n-1)
#print(fact(3))
if __name__=='__main__':
    import doctest
    doctest.testmod()
