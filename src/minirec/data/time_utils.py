from datetime import datetime
from zoneinfo import ZoneInfo

# 数据所在的业务时区。淘宝数据按北京时间划分日期。
DATA_TZ = ZoneInfo("Asia/Shanghai")


def ts_to_ds(ts: int) -> str:
    """把 Unix 时间戳（秒）转换成业务时区下的日期分区字符串，格式 YYYY-MM-DD。"""
    return datetime.fromtimestamp(ts, tz=DATA_TZ).strftime("%Y-%m-%d")