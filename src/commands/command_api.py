"""
Модуль с интерфейсом всех утилит,
которые могут быть запущены в
интерпретаторе
"""

from typing import List, IO
from abc import ABC, abstractmethod
from src.enviroment.enviroment import Environment


class ICommand(ABC):
    """
    Базовый класс всех утилит.
    """
    @abstractmethod
    def run(self, args: List[str], inp: IO, out: IO, err: IO, env: Environment) -> int:
        """
        Метод, который запускает выполнение утилиты. Все наследники
        ICommand в этом методе должны определить всё выполнение команды.
        :param args: Аргументы, которые были переданы в командной строке.
        Подразумевается, что все переменные были подставлены и все кавычки
        были расскрыты, и об этом не нужно беспокоится.
        :param inp: Поток ввода. Если комаде требуется что-то считать (например,
        cat без аргументов) то она должна читать именно с этого потока.
        :param out: Поток вывода. Аналогично писать команда должна в этот поток.
        :param err:  Поток ошибок.
        :param env: Окружение. В этом окружении находится набор переменных, к которым
        можно обращаться, а так же добавлять новые по необходимости.
        :return: Код возврата.
        """


class IBasicCommand(ICommand):
    """
    Интерфейс для базовых утилит, у которых есть имя.
    """
    @staticmethod
    @abstractmethod
    def get_name() -> str:
        pass
