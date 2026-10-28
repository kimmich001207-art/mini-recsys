import pytest

from minirec.data.time_utils import ds_range, ts_to_ds


def test_midnight_belongs_to_that_day():
    # 1511539200 是北京时间 2017-11-25 00:00:00，即数据集的起始时刻
    assert ts_to_ds(1511539200) == "2017-11-25"


def test_one_second_before_midnight_belongs_to_previous_day():
    # 早 1 秒，就应该还是前一天
    assert ts_to_ds(1511539199) == "2017-11-24"

def test_ds_range_within_month():
    assert ds_range("2017-11-25", "2017-11-27") == [
        "2017-11-25",
        "2017-11-26",
        "2017-11-27",
    ]
def test_ds_range_different_month():
    assert ds_range("2017-11-30", "2017-12-02") == [
        "2017-11-30",
        "2017-12-01",
        "2017-12-02",
    ]
def test_ds_range_same_day():
    assert ds_range("2017-11-25", "2017-11-25") == ["2017-11-25"]

def test_ds_range_accepts_compact_format():
    assert ds_range("20171130", "2017-12-02") == ["2017-11-30", "2017-12-01", "2017-12-02"]

def test_ds_range_start_after_end_raises():
    with pytest.raises(ValueError):
        ds_range("2017-12-02", "2017-11-30")


@pytest.mark.parametrize(
    "ts, expected",
    [
        (1511539200 + 8 * 3600, "2017-11-25"),       # 北京时间 08:00
        (1511539200 + 86400 - 1, "2017-11-25"),      # 北京时间 23:59:59
        (1511539200 + 86400, "2017-11-26"),          # 北京时间次日 00:00
    ],
)
def test_various_times_within_a_day(ts, expected):
    assert ts_to_ds(ts) == expected