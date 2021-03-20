from datetime import date


def str_to_date(data: str) -> data:
    datas = data.split("-")
    return date(datas[0], datas[1], datas[2])
