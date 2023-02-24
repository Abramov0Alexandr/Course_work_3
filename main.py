from utils import functions


def main():
    raw_data = functions.json_reader()
    pre_sorted_data_list = functions.check_data_for_empty_dict(raw_data)
    sorted_data_list = functions.sort_data_by_time(pre_sorted_data_list)
    final_data = [i for i in sorted_data_list if i['state'] == 'EXECUTED'][: 5]

    for i in final_data:

        print(f"{functions.date_editor(i)} {i.get('description')}\n"
              f"{functions.users_account_editor(i).strip()} -> {functions.beneficiary_account_editor(i)}\n"
              f"{i.get('operationAmount')['amount']} {i.get('operationAmount')['currency']['name']}\n")


if __name__ == '__main__':
    main()
