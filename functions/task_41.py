__author__ = 'nxn3370'
# 41 Find Task by Id

from core.sg_connect import sg
def task_41( task_id, quiet = "0" ):
    find_res = sg.find_one( 'Task', [[ 'id', 'is', int( task_id ) ]], ['id', 'content'] )
    tmp_str = str( find_res ).lower()
    res = tmp_str.find( "none" )
    #print find_res

    if( res != 0 ):
        print ( "Found match Task \"" + find_res['content'] + "\" #" + str( find_res['id'] ) + "." )
        res = 0
    else:
        if( int(quiet) != 1 ):
            print ( "Fail to find Task id #" + task_id + "." )
        res = -1

    return res