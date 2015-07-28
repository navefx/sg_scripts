__author__ = 'Nave'

from core.sg_connect import sg

def task_0():
    result = sg.find_one( "Asset", [['code','is_not','aabbcc']])
    if( cmp( result['id'], "" ) != 0 ):
        print "Ready to go."
        return 0
    else:
        print "Something Wrong."
        return 1
