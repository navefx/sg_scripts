__author__ = 'nxn3370'
# 12 Create Asset

from core.sg_connect import sg

def task_12( ):
    data = {
        'project': {"type":"Project","id": 4},
        'code': 'test',
        'sg_asset_type': 'Character / 角色',
        'description': 'script create',
        'sg_status_list': 'n_wtg'
    }
    result = sg.create('Asset', data)

    print result


