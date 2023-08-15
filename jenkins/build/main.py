import utils.constant as constant
import os

from utils.csv_to_db import ALARMLIST
from dotenv import load_dotenv

load_dotenv()

ALARMLIST = ALARMLIST(
        path=constant.ALARMLIST_PATH,
        server=os.getenv('SERVER'),
        database=os.getenv('DATABASE'),
        user_login=os.getenv('USER_LOGIN'),
        password=os.getenv('PASSWORD'),
        table=constant.ALARMLIST_TABLE,
        table_columns=constant.ALARMLIST_TABLE_COLUMNS,
        table_log=constant.ALARMLIST_TABLE_LOG,
        table_columns_log=constant.ALARMLIST_TABLE_COLUMNS_LOG,
        notify_token=os.getenv('NOTIFY_TOKEN'),
    )


ALARMLIST.run()