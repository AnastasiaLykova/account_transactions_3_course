from utils import get_sorted_id, get_main_text, hide_card_number
import pytest


@pytest.fixture
def operations():
    return [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
  }]


@pytest.fixture
def id_list():
    return [441945886, 41428829, 587085106]


def test_hide_card_number():
    assert hide_card_number("Счет 48943806953649539453") == "Счет **9453"
    assert hide_card_number("Visa Gold 7756673469642839") == "Visa Gold 7756 67** **** 2839"


def test_get_main_text(operations, id_list):
    assert get_main_text(operations, id_list) == \
           {441945886: '26.08.2019 Перевод организации Maestro 1596 83** **** 5199 -> Счет **9589 31957.58 руб.',
            41428829: '03.07.2019 Перевод организации MasterCard 7158 30** **** 6758 -> Счет **5560 8221.37 USD',
            587085106: '23.03.2018 Открытие вклада Счет **2431 48223.05 руб.'}


def test_get_sorted_id(operations):
    assert get_sorted_id(operations) == [441945886, 41428829, 587085106]
