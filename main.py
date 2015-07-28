__author__ = 'nxn3370'

# import libraries
import os,sys

#------------------------------------
#   First Args Translation list:
#
#       0 Link Test
#
#       1 Assets:
#           10 Find Asset by Name
#           11 Find Asset by Id
#           12 Create Asset
#           13 Delete Asset
#           14 Update Asset
#
#       2 Shots:
#           20 Find Shot by Name
#           21 Find Shot by Id
#           22 Create Shot
#           23 Delete Shot
#           24 Update Shot
#
#       3 Sequences:
#           30 Find Sequences by Name
#           31 Find Sequences by Id
#           32 Create Sequences
#           33 Delete Sequences
#           34 Update Sequences
#
#       4 Tasks:
#           40 Find Task by Name
#           41 Find Task by Id
#           42 Create Task
#           43 Delete Task
#           44 Update Task
#
#       5 Versions:
#           50 Find Version by Name
#           51 Find Version by id
#           52 Create Version
#           53 Delete Version
#           54 Update Version
#
#       6 People:
#           60 Find People by Name
#           61 Find People by id
#           62 Get People Status
#           63 Update People
#           64 Link People to ...
#
#       7 Analyzer:
#           70 Analyze Project
#           71 Analyze Asset
#           72 Analyze Shot
#           73 Analyze Sequence
#           74 Analyze Task
#           75 Analyze Version
#           76 Analyze People
#
#       76000 PLE:
#           76100 APC:
#               76110 APC SQL Connections:
#                  76110 APC SQL Connection Linker
#                  76112 APC SQL Connection Breaker
#               76120 APC SQL IO:
#                   76121 APC SQL Get Data
#                   76122 APC SQL Insert Data
#                   76123 APC SQL Update Data
#                   76124 APC SQL Delete Data
#
#           76900 Admin:
#               76910 Super Admin Login
#               76920 Super Admin unLogin
#               76930 Super Core:
#                   76931 Create Project Local Data System
#                   76932 Lock/ unLock Project Local Data System
#                   76933 Break-Down All Connections
#                   76934 Restart All Services
#                   76935 Shutdown All Services
#                   76936 Clear Local Data
#                   76937 Clear Shotgun Data
#                   76938 Backup Local Data
#                   76939 Backup Shotgun Data
#
#
#------------------------------------

# 10 Find Asset by Name
if( sys.argv[1] == "10" ):
    import functions.task_10 as job
    if( len(sys.argv) == 4 ):
        job_res = job.task_10( sys.argv[2], sys.argv[3] )
    else:
        job_res = job.task_11( sys.argv[2] )
    print "Job exited code : " + str( job_res ) + "."

# 11 Find Asset by Id
if( sys.argv[1] == "11" ):
    import functions.task_11 as job
    if( len(sys.argv) == 4 ):
        job_res = job.task_11( sys.argv[2], sys.argv[3] )
    else:
        job_res = job.task_11( sys.argv[2] )
    print "Job exited code : " + str( job_res ) + "."

# 12 Create Asset
if( sys.argv[1] == "12" ):
    import functions.task_12 as job
    res = job.task_12()

# 41 Find Task by Id
if( sys.argv[1] == "41" ):
    import functions.task_41 as job
    if( len(sys.argv) == 4 ):
        job_res = job.task_41( sys.argv[2], sys.argv[3] )
    else:
        job_res = job.task_41( sys.argv[2] )
    print "Job exited code : " + str( job_res ) + "."

# 44 Update Task
if( sys.argv[1] == "44" ):
    import functions.task_44 as job
    if( len(sys.argv) == 6 ):
        job_res = job.task_44( sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] )
    else:
        job_res = job.task_44( sys.argv[2], sys.argv[3], sys.argv[4] )
    print "Job exited code : " + str( job_res ) + "."
