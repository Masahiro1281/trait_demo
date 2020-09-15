import datetime


datetime_1 = "2020/09/01 00:00:00"
datetime_2 = "2020/09/01 00:01:00"
datetime_3 = "2020/09/01 00:02:00"
datetime_4 = "2020/09/01 00:03:00"
datetime_5 = "2020/09/01 00:04:00"
datetime_6 = "2020/09/01 00:05:00"
datetime_7 = "2020/09/01 00:06:00"
datetime_8 = "2020/09/07 00:07:00"

datetime_list_1 = [
    datetime_1,
    datetime_2,
    datetime_3,
    datetime_4,
    datetime_5,
    datetime_6,
    datetime_7,
    datetime_8,
]

datetime_list_2 = [
    [datetime_1],
    [datetime_2],
    [datetime_3],
    [datetime_4],
    [datetime_5],
    [datetime_6],
    [datetime_7],
    [datetime_8],
]


def str_to_timestamp(date_str):
    date_dt = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M:%S')
    return date_dt.timestamp()


def str_to_datetime(date_str):
    return datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M:%S')


date_dt_list_1 = [str_to_timestamp(idate) for idate in datetime_list_1]
date_dt_list_2 = [str_to_timestamp(idate[0]) for idate in datetime_list_2]

date_tm_list_1 = [str_to_datetime(idate) for idate in datetime_list_1]
date_tm_list_2 = [str_to_datetime(idate[0]) for idate in datetime_list_2]
