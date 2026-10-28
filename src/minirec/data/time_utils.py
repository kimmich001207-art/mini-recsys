from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

# 数据所在的业务时区。淘宝数据按北京时间划分日期。
DATA_TZ = ZoneInfo("Asia/Shanghai")


def ts_to_ds(ts: int) -> str:
    """把 Unix 时间戳（秒）转换成业务时区下的日期分区字符串，格式 YYYY-MM-DD。"""
    return datetime.fromtimestamp(ts, tz=DATA_TZ).strftime("%Y-%m-%d")

def ds_range(start: str, end: str) -> list[str]:
    current = date.fromisoformat(start)
    end_date = date.fromisoformat(end)
    if current > end_date:
        raise ValueError(f"start ({start}) must be <= end ({end})")
    list_of_dates = []

    while current <= end_date:
        list_of_dates.append(current.isoformat())
        current = current + timedelta(days=1)
    return list_of_dates
