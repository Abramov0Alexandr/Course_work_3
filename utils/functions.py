import time
import requests
from operator import itemgetter


BANK_TRANSACTION_DATA = 'https://api.npoint.io/84633d18dad22794d84b'


def json_reader() -> list:
    """
    Функция для получения исходных данных
    :return: Списковый словарь
    """

    response = requests.get(BANK_TRANSACTION_DATA)
    result = response.json()
    return result


def check_data_for_empty_dict(data_list: list) -> list:
    """
    Функция поверяет переданный, в качестве аргумента списковый словарь, на наличие пустых словарей.
    :param data_list: Списковый словарь
    :return: Сформированный списковый словарь, в котором отсутствуют пустые словари, если такие были
    """
    list_after_check = []

    for i in data_list:
        if len(i) != 0:
            list_after_check.append(i)
        else:
            continue

    return list_after_check


def sort_data_by_time(data_dict: list, key='date') -> list:
    """
    Функция сортирует словарь по переданному в аргумент ключу (по умолчанию сортировка происходит по дате)
    :param data_dict: Словари, которые необходимо отсортировать.
    :param key: Ключ, по которому будет происходить сортировка
    :return: Отсортированный словарь
    """

    pre_sorted_data = data_dict

    sorted_data = sorted(pre_sorted_data, key=itemgetter(key), reverse=True)
    return sorted_data


def date_editor(data_dict: dict) -> str:
    """
    Функция форматирует полученную дату к виду ДД.ММ.ГГГГ
    :param data_dict: Словарь, в котором необходимо произвести форматирование даты
    :return: Полученный словарь с отформатированной датой
    """
    source = data_dict.get('date')

    if source:
        raw_date = source[: source.find('T')]
        pre_format_date = time.strptime(raw_date, "%Y-%m-%d")
        formatted_date = time.strftime("%d.%m.%Y", pre_format_date)

    else:
        formatted_date = 'Ошибка прочтения даты'

    return formatted_date


def users_account_editor(data_dict: dict) -> str:
    """
    Функция принимает в качестве аргумента словарь, в котором содержится информация о
    банковской карте пользователя и его счете. Банковская карта не шифруется и выводится
    полностью. Счет карты или лицевой счет шифруется и показывается не полностью (видны
    первые 6 и последние 4 цифры)
    :param data_dict: Словарь, содержащий информацию о банковской карте пользователя и
    номер счета
    :return: Наименование банковской карты или счета, а также шифрованный номер карты или
    лицевого счета
    """
    spaces_idx = [4, 9, 14, 19]
    source = data_dict.get('from')

    if source is not None:

        #: Кодировка номера СЧЕТА
        if len(''.join(list(source.split()[1]))) == 20:
            name_card = source.split()[0]
            account_number = list(source.split()[1])
            account_number[6:16] = '**********'

        #: Кодировка номера карты, если в названии карты 1 слова (Maestro)
        elif len(source.split(' ')) == 2:
            name_card = source.split()[0]
            account_number = list(source.split()[1])

        #: Кодировка номера карты, если в названии карты 2 слова (Master Card)
        elif len(source.split(' ')) == 3:
            name_card = ' '.join(source.split()[0:2])
            account_number = list(source.split(' ')[2])

        account_number[6:12] = '******'

        #: Цикл на вставку пробелов по заранее известным индексам
        while spaces_idx:
            account_number.insert(
                spaces_idx.pop(0), ' ')
        coded_account = ''.join(account_number)

    #: Данное условие срабатывает, если происходит открытие вклада
    else:
        name_card = 'Вклад'
        coded_account = 'открыт'

    return f"{name_card} {coded_account.strip()}"


def beneficiary_account_editor(data_dict: dict) -> str:
    """
    Функция кодирует счет получателя таким образом, что пользователь видит 6 последних цифр номера счета,
    на который была произведена транзакция. 6 последних цифр также видны не полностью, первые 2 цифры зашифрованы
    звездочками, а 4 последних отображаются открыто
    :param data_dict: Словарь, в котором содержится информация о наименовании карты(счета) и лицевого счета получателя
    :return: Наименование карты(счета) и последние цифры счета в формате **1111
    """
    source = data_dict.get('to')

    #: Кодировка номера карты, если в названии карты 1 слова (Maestro)
    if len(source.split(' ')) == 2:
        name_card = source.split()[0]
        account_number = source.split()[1]

    #: Кодировка номера карты, если в названии карты 2 слова (Master Card)
    elif len(source.split(' ')) == 3:
        name_card = ' '.join(source.split()[0:2])
        account_number = source.split(' ')[2]

    account_number = list(account_number[-6:])
    account_number[:2] = '**'
    coded_account = ''.join(account_number)

    return f"{name_card} {coded_account}"
