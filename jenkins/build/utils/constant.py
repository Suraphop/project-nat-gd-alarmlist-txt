# data ALARMLIST
ALARMLIST_PATH = 'D:/data/data_alarmlist/gd' #'/data/ALARMLIST_ng' ,'D:/data/ALARMLIST_ng'
ALARMLIST_TABLE = 'data_alarmlist'
ALARMLIST_TABLE_COLUMNS ='''
                registered_at datetime,
                topic varchar(50),
                occurred varchar(50),
                restored varchar(50),
                time_diff int,
                mc_no varchar(50),'''
            
ALARMLIST_TABLE_LOG = 'log_alarmlist'
ALARMLIST_TABLE_COLUMNS_LOG ='''
            registered_at datetime,
	        status varchar(50),
            file_name varchar(100),
            process varchar(50),
            message varchar(50),
            error varchar(MAX),
            '''

#LOG status
STATUS_OK = 'ok'
STATUS_ERROR = 'error'
STATUS_INFO = 'info'