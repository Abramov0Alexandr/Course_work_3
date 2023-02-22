import time
import requests
from operator import itemgetter


def json_reader() -> list:

    response = requests.get('https://api.npoint.io/27390f0e02c8539a928e')
    result = response.json()
    return result


def sort_data_by_time(data_dict: list) -> list:

    pre_sorted_data = data_dict

    try:
        sorted_data = sorted(pre_sorted_data, key=itemgetter('date'), reverse=True)
        return sorted_data

    except KeyError:
        print('Ошибка прочтения даты в массиве данных')