__author__ = 'nxn3370'
# 11 Find Asset by Id

from core.sg_connect import sg
def task_11( ass_id, quiet = "0" ):
    find_res = sg.find_one( 'Asset', [[ 'id', 'is', int( ass_id ) ]], ['id', 'code'] )
    tmp_str = str( find_res ).lower()
    res = tmp_str.find( "none" )
    #print find_res

    if( res != 0 ):
        print ( "Found match asset \"" + find_res['code'] + "\" #" + str( find_res['id'] ) + "." )
        res = 0
    else:
        if( int(quiet) != 1 ):
            print ( "Fail to find Asset id #" + ass_id + "." )
        res = -1

    return res