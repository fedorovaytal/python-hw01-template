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

def func1(url: str = 'https://ru.wikipedia.org/') -> str:
    """
    С помощью пакета requests скачавает страницу с сайта и возвращает её
        HTML-код
    :param url: Адрес страницы, которую нужно скачать, по умолчанию:
        https://ru.wikipedia.org/
    :return: HTML-код страницы
    """
    return requests.get(url).text


def func2(html_text: str) -> List[str]:
    """
    Извлекает из HTML-кода текст с помощью библиотеки BeautifulSoup
    :param html_text: HTML-код страницы
    :return: список слов извлечённых из страницы
    """
    # Извлекаем html-код страницы
    soup = BeautifulSoup(html_text, 'html.parser')
    # Извлекаем текст страницы с помощью метода get_text
    text = soup.get_text(' ', True)
    return text.split(sep=' ')

def func3(words: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество повторов слов
    :param words: Список из слов с повторами
    :return: Словарь с количеством повторов слов
    """
    # Инициализируем словарь myDict
    myDict = dict()
    
    for word in words:
        # Оставляем только буквы в строке
        str = "".join(char for char in word if char.isalpha())
        
        # Если строка уже добавлена в словарь, то увеличиваем значение ключа
        if str in myDict:
            myDict[str] += 1
        # Если строка отсутствует, то добавляем его в словарь
        else:
            myDict[str] = 1
    return myDict


def main():
    """ Главная функция """
    html = func1()
    words = func2(html)
    freq = func3(words)
    
    pprint(freq)


if __name__ == '__main__':
    main()
