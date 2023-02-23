import time
import requests
from operator import itemgetter


def json_reader() -> list:

    response = requests.get('https://api.npoint.io/84633d18dad22794d84b')
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


def users_account_editor(data_dict: dict) -> str:
    spaces_idx = [4, 9, 14, 19]
    source = data_dict.get('from')

    if source is not None:

        if len(''.join(list(source.split()[1]))) == 20:
            name_card = source.split()[0]
            account_number = list(source.split()[1])
            account_number[6:16] = '**********'

        elif len(source.split(' ')) == 2:
            name_card = source.split()[0]
            account_number = list(source.split()[1])

        elif len(source.split(' ')) == 3:
            name_card = ' '.join(source.split()[0:2])
            account_number = list(source.split(' ')[2])

        account_number[6:12] = '******'

        while spaces_idx:
            account_number.insert(
                spaces_idx.pop(0), ' ')
        coded_account = ''.join(account_number)

    else:
        name_card = 'Вклад'
        coded_account = 'открыт'

    return f"{name_card} {coded_account}"


def beneficiary_account_editor(data_dict: dict) -> str:
    source = data_dict.get('to')

    if len(source.split(' ')) == 2:
        name_card = source.split()[0]
        account_number = source.split()[1]

    elif len(source.split(' ')) == 3:
        name_card = ' '.join(source.split()[0:2])
        account_number = source.split(' ')[2]

    account_number = list(account_number[-6:])
    account_number[:2] = '**'
    coded_account = ''.join(account_number)

    return f"{name_card} {coded_account}"