from utils import functions
import pytest


def test_json_reader():
    url = functions.BANK_TRANSACTION_DATA

    assert functions.json_reader(url)


def test_empty_json_dict():

    testing_data = [{}, {1: 'a', 2: 'b', 3: 'c'}]
    desired_result = [{1: 'a', 2: 'b', 3: 'c'}]

    assert functions.check_data_for_empty_dict(testing_data) == desired_result


def test_sort_by_time():

    testing_data = [{'date': '2017.05.11.'}, {'date': '2019.04.05.'}, {'date': '2016.01.04'}]
    desired_result = [{'date': '2019.04.05.'}, {'date': '2017.05.11.'}, {'date': '2016.01.04'}]

    assert functions.sort_data_by_time(testing_data) == desired_result


def test_date_editor_normal():

    testing_data = {'date': '2019-12-08T22:46:21.935582'}
    desired_result = '08.12.2019'

    assert functions.date_editor(testing_data) == desired_result


def test_date_editor_exception():

    testing_data = {}
    desired_result = 'Ошибка прочтения даты'

    assert functions.date_editor(testing_data) == desired_result


def test_user_account_number():

    testing_data = {'from': 'Счет 49304996510329747621'}
    desired_result = 'Счет 4930 49** **** **** 7621'

    assert functions.users_account_editor(testing_data) == desired_result


def test_users_account_short_name_card():

    testing_data = {'from': 'МИР 5211277418228469'}
    desired_result = 'МИР 5211 27** **** 8469'

    assert functions.users_account_editor(testing_data) == desired_result


def test_users_account_long_name_card():

    testing_data = {'from': 'Visa Classic 6831982476737658'}
    desired_result = 'Visa Classic 6831 98** **** 7658'

    assert functions.users_account_editor(testing_data) == desired_result


def test_users_account_empty_source():

    testing_data = {'from': None}
    desired_result = 'Вклад открыт'

    assert functions.users_account_editor(testing_data) == desired_result


def test_beneficiary_account_editor_exceptions():

    with pytest.raises(AttributeError):
        functions.beneficiary_account_editor({})


def test_beneficiary_short_name_card():

    testing_data = {'to': 'Maestro 3806652527413662'}
    desired_result = 'Maestro **3662'

    assert functions.beneficiary_account_editor(testing_data) == desired_result


def test_beneficiary_long_name_card():

    testing_data = {'to': 'Visa Classic 1435442169918409'}
    desired_result = 'Visa Classic **8409'

    assert functions.beneficiary_account_editor(testing_data) == desired_result
