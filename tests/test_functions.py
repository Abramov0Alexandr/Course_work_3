from utils import functions
import pytest


def test_json_reader():

    assert functions.json_reader() != []


def test_empty_json_dict():

    testing_data = [{}, {1: 'a', 2: 'b', 3: 'c'}]
    data_after_test = [{1: 'a', 2: 'b', 3: 'c'}]

    assert functions.check_data_for_empty_dict(testing_data) == data_after_test


def test_sort_by_time():

    testing_data = [{'date': '2017.05.11.'}, {'date': '2019.04.05.'}, {'date': '2016.01.04'}]
    data_after_test = [{'date': '2019.04.05.'}, {'date': '2017.05.11.'}, {'date': '2016.01.04'}]

    assert functions.sort_data_by_time(testing_data) == data_after_test


def test_date_editor_normal():

    testing_data = {'date': '2019-12-08T22:46:21.935582'}
    data_after_test = '08.12.2019'

    assert functions.date_editor(testing_data) == data_after_test


def test_date_editor_exception():

    testing_data = {}
    data_after_test = 'Ошибка прочтения даты'

    assert functions.date_editor(testing_data) == data_after_test


def test_user_account_number():

    testing_data = {'from': 'Счет 49304996510329747621'}
    data_after_test = 'Счет 4930 49** **** **** 7621'

    assert functions.users_account_editor(testing_data) == data_after_test


def test_users_account_short_name_card():

    testing_data = {'from': 'МИР 5211277418228469'}
    data_after_test = 'МИР 5211 27** **** 8469'

    assert functions.users_account_editor(testing_data) == data_after_test


def test_users_account_long_name_card():

    testing_data = {'from': 'Visa Classic 6831982476737658'}
    data_after_test = 'Visa Classic 6831 98** **** 7658'

    assert functions.users_account_editor(testing_data) == data_after_test


def test_users_account_empty_source():

    testing_data = {'from': None}
    data_after_test = 'Вклад открыт'

    assert functions.users_account_editor(testing_data) == data_after_test


def test_beneficiary_account_editor_exceptions():

    with pytest.raises(AttributeError):
        functions.beneficiary_account_editor({})


def test_beneficiary_short_name_card():

    testing_data = {'to': 'Maestro 3806652527413662'}
    data_after_test = 'Maestro **3662'

    assert functions.beneficiary_account_editor(testing_data) == data_after_test


def test_beneficiary_long_name_card():

    testing_data = {'to': 'Visa Classic 1435442169918409'}
    data_after_test = 'Visa Classic **8409'

    assert functions.beneficiary_account_editor(testing_data) == data_after_test
