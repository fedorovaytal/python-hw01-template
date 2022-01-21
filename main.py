# 123
"""
Домашнее задание 1
Перед выполнением нужно:
1. создать виртуальное окружение
2. установить в него библиотеки с помощью команды `pip install -r requirements.txt`
"""
from pprint import pprint
from typing import List, Dict
import requests
from bs4 import BeautifulSoup
from collections import Counter



def func1(url: str = 'https://ru.wikipedia.org/') -> str:
    """
    С помощью пакета requests скачавает страницу с сайта и возвращает её
        HTML-код
    :param url: Адрес страницы, которую нужно скачать, по умолчанию:
        https://ru.wikipedia.org/
    :return: HTML-код страницы
    """
    x = requests.get(url).text
    return x


def func2(html_text: str) -> List[str]:
    """
    Извлекает из HTML-кода текст с помощью библиотеки BeautifulSoup
    :param html_text: HTML-код страницы
    :return: список слов извлечённых из страницы
    """
    x = BeautifulSoup(html_text, features="html.parser").get_text().splitlines()
    a = []
    for i in x:
        for j in i.split(' '):
            if j != '':
                a.append(j)
    
    return a


def func3(words: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество повторов слов
    :param words: Список из слов с повторами
    :return: Словарь с количеством повторов слов
    """
    freq = []
    while words != []:
        i = words[0]
        count = 0
        for j in words:
            if i == j:
                count += 1
        for a in range(count):
            words.remove(i)
        freq.append((i, count))

    return freq

def main():
    """ Главная функция """
    html = func1()
    words = func2(html)
    freq = func3(words)
    freq.sort(key = lambda x: (-x[1], x[0]))
    print(freq)


if __name__ == '__main__':
    main()
