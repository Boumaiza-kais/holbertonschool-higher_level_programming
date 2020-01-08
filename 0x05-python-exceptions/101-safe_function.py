#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        k = fct(*args)
    except Exception as err:
        k = None
        print('Exception: {}'.format(err), file=sys.stderr)
    return k
