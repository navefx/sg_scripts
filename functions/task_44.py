__author__ = 'nxn3370'
# Job 44 Task Update

from core.sg_connect import sg
def task_44( task_id, task_data, task_stname ):
    t_stat = { 'id': int( task_id ), 'up': task_data, 'stat': task_stname }
    t_data = { 'sg_status_list': t_stat['up'] }
    result = sg.update('Task', t_stat['id'], t_data)
    res = cmp( t_stat['up'], result['sg_status_list'])
    task_name = sg.find_one( 'Task', [[ 'id', 'is', t_stat['id'] ]], ['content'] )

    if( res == 0 ):
        print ( "Task \"" + task_name['content'] + "\" #" + str(result['id']) + "'s status is update to \"" + t_stat['stat'] + "\"" )
    else:
        print ( "Fail to update Task #" + str(result['id']) + "'s status  to \"" + t_stat['name'] + "\"" )

    return res