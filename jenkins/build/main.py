import utils.constant as constant
import os

from utils.csv_to_db import TALYSURF
from dotenv import load_dotenv

load_dotenv()

talysurf = TALYSURF(
        path=constant.TALYSURF_PATH,
        server=os.getenv('SERVER'),
        database=os.getenv('DATABASE'),
        user_login=os.getenv('USER_LOGIN'),
        password=os.getenv('PASSWORD'),
        table=constant.TALYSURF_TABLE,
        table_columns=constant.TALYSURF_TABLE_COLUMNS,
        table_log=constant.TALYSURF_TABLE_LOG,
        table_columns_log=constant.TALYSURF_TABLE_COLUMNS_LOG,
        line_notify_token=os.getenv('LINE_NOTIFY_TOKEN'),
    )


talysurf.run()