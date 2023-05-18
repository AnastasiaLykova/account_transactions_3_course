import json
import os


def load_json():
    """Загружает json файл и возвращает в виде списка со словарями"""
    json_path = os.path.join("..", "operations.json")
    with open(json_path, "r", encoding="utf-8") as file:
        return json.loads(file.read())
