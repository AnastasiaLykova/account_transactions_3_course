import json
import os


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
