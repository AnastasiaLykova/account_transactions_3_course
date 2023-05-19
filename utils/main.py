from utils import load_json, get_sorted_id, get_main_text

# Загрузка исходных данных
operations = load_json()

# Сортировка по дате и выборка 5 выполненных транзакций
id_list = get_sorted_id(operations)

# Вывод данных
for i in get_main_text(operations, id_list).values():
    print(i, end="\n\n")
