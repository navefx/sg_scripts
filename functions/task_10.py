__author__ = 'nxn3370'
# Job 10 Find Asset by Name

from core.sg_connect import sg
def task_10( ass_name, quiet = "0" ):
    find_res = sg.find_one( 'Asset', [[ 'code', 'is', ass_name ]], ['id', 'code'] )
    tmp_str = str( find_res ).lower()
    res = tmp_str.find( "none" )

    if( res != 0 ):
        print ( "Found match asset \"" + find_res['code'] + "\" #" + str( find_res['id'] ) + "." )
        res = 0
    else:
        if( int(quiet) != 1 ):
            print ( "Fail to find Asset named \"" + ass_name + "\"." )
        res = -1

    return res