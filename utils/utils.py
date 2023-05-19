import json
import os
from datetime import datetime


def load_json():
    """Загружает json файл и возвращает в виде списка со словарями"""
    json_path = os.path.join("..", "operations.json")
    with open(json_path, "r", encoding="utf-8") as file:
        return json.loads(file.read())


def hide_card_number(unhidden_number):
    """Принимает данные о счете или карте в формате строки вида:
    счет номер/название карты номер
    возвращает замаскированные данные счета или карты"""

    split_description = unhidden_number.split(" ")

    if len(split_description[-1]) == 20:
        account_number = split_description[-1]
        cut_account_number = account_number[-4:]
        return f"{' '.join(split_description[:-1])} **{cut_account_number}"

    if len(split_description[-1]) == 16:
        card_number = split_description[-1]
        cut_card_number_left = card_number[:4] + " " + card_number[4:6]
        cut_card_number_right = card_number[-4:]
        return f"{' '.join(split_description[:-1])} {cut_card_number_left}** **** {cut_card_number_right}"


def get_main_text(operations, id_list):
    """Принимает исходные данные в виде списка со словарями (operations)
    и отсортированную выборку id транзакции (id_list).
    Возвращает словарь с ключами id (в той же сортировке как на входе),
    и с текстом для вывода:
    <дата перевода> <описание перевода> <откуда> -> <куда> <сумма перевода> <валюта>"""

    main_text_dict = {}

    for transaction_id in id_list:
        main_text_dict[transaction_id] = ''

    for operation in operations:
        if 'id' in operation.keys() and operation['id'] in id_list:
            if operation['description'] == 'Открытие вклада':
                hiden_number_from = ''
            else:
                hiden_number_from = hide_card_number(operation['from']) + " -> "
            hiden_number_to = hide_card_number(operation['to'])
            main_text_dict[operation['id']] = (f"{'.'.join(reversed((operation['date'][:10]).split('-')))} "
                                               f"{operation['description']} "
                                               f"{hiden_number_from}"
                                               f"{hiden_number_to} "
                                               f"{operation['operationAmount']['amount']} "
                                               f"{operation['operationAmount']['currency']['name']}")
    return main_text_dict


def get_sorted_id(operations):
    """Получает исходные данные в виде списка со словарями,
    возвращает список (id) последних 5 выполненых транзакций,
    отсортированных по дате"""
    correct_operations = operations.copy()
    if {} in correct_operations:
        correct_operations.remove({})

    sorted_list = sorted(correct_operations, key=lambda x:
                         datetime.strptime(x['date'][:19], '%Y-%m-%dT%H:%M:%S'), reverse=True)
    id_list = []
    for item in sorted_list:
        if len(id_list) < 5 and item['state'] == 'EXECUTED':
            id_list.append(item['id'])
    return id_list
