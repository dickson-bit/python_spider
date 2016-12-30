# coding: utf-8
__author__ = 'guodl'


def var_func(a, b, *more_args, **more_kw_args):

    print a + b;

    print "begin more args"
    for args in more_args:
        print args

    print "begin more dict args"
    for key in more_kw_args:
        #print more_kw_args[key]
        print key
        print more_kw_args[key]


var_func(1, 2, 3, 4, test=5)


