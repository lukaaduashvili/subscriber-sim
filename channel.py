from typing import List

from observer_interfaces import Subject, Observer


class Channel(Subject):

    _subscribers: List[Observer] = []

    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def attach(self, observer: Observer) -> None:
        self._subscribers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._subscribers.remove(observer)

    def notify(self) -> None:
        for observer in self._subscribers:
            observer.update(self)
