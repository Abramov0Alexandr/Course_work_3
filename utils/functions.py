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


def date_editor(data_dict: dict) -> str:
    source = data_dict.get('date')

    if source:
        raw_date = source[: source.find('T')]
        pre_format_date = time.strptime(raw_date, "%Y-%m-%d")
        formatted_date = time.strftime("%d.%m.%Y", pre_format_date)

    else:
        formatted_date = 'Ошибка прочтения даты'

    return formatted_date
