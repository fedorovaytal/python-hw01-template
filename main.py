"""
Домашнее задание 1
Перед выполнением нужно:
1. создать виртуальное окружение
2. установить в него библиотеки с помощью команды `pip install -r requirements.txt`
"""
from pprint import pprint
from typing import List, Dict


def func1(url: str = 'https://ru.wikipedia.org/') -> str:
    """
    С помощью пакета requests (https://docs.python-requests.org/en/latest/)
        скачавает страницу с сайта и возвращает её HTML-код
    :param url: Адрес страницы, которую нужно скачать, по умолчанию:
        https://ru.wikipedia.org/
    :return: HTML-код страницы
    """


def func2(html_text: str) -> List[str]:
    """
    Извлекает из HTML-кода текст с помощью библиотеки BeautifulSoup
        (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    :param html_text: HTML-код страницы
    :return: список слов извлечённых из страницы
    """


def func3(words: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество повторов слов
    :param words: Список из слов с повторами
    :return: Словарь с количеством повторов слов
    """


def main():
    """ Главная функция """
    html = func1()
    words = func2(html)
    freq = func3(words)
    pprint(freq)


if __name__ == '__main__':
    main()
