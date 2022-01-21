from pprint import pprint
from typing import List, Dict
import requests
from bs4 import BeautifulSoup


def func1(url: str = 'https://ru.wikipedia.org/') -> str:

    return requests.get(url).text


def func2(html_text: str) -> List[str]:


    soup = BeautifulSoup(html_text, 'html.parser')

    text = soup.get_text(' ', True)
    return text.split(sep=' ')


def func3(words: List[str]) -> Dict[str, int]:


    myDict = dict()

    for word in words:

        str = "".join(char for char in word if char.isalpha())

        if str in myDict:
            myDict[str] += 1

        else:
            myDict[str] = 1
    return myDict


def main():

    html = func1()
    words = func2(html)
    freq = func3(words)

    pprint(freq)


if __name__ == '__main__':
    main()