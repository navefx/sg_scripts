__author__ = 'nxn3370'
# Job 44 Task Update

from core.sg_connect import sg
import functions.task_41 as job

def task_44( task_id, task_data, task_stname, quiet = "0"  ):
    # find task
    res = job.task_41( task_id, 1 )

    if( res == 0 ):
        t_stat = { 'id': int( task_id ), 'up': task_data, 'stat': task_stname }
        t_data = { 'sg_status_list': t_stat['up'] }

        result = sg.update('Task', t_stat['id'], t_data)
        tmp_str = str( result ).lower()
        res = tmp_str.find( "none" )

        if( res != 0 ):
            task_name = sg.find_one( 'Task', [[ 'id', 'is', t_stat['id'] ]], ['content'] )
            print ( "Task \"" + task_name['content'] + "\" #" + str(result['id']) + "'s status is update to \"" + t_stat['stat'] + "\"" )
            res = 0
        else:
            res = -1
            if( int(quiet) != 1 ):
                print ( "Fail to update Task #" + task_id + "'s status  to \"" + task_stname + "\"" )
        return res

    else:
        if( int(quiet) != 1 ):
            print ( "Fail to found Task #" + task_id + "." )
        res = -1
        return res



