from typing import List

from observer_interfaces import Observer, Subject
from subscriber_db import FileDb


class Channel(Subject):
    def __init__(self, name: str) -> None:
        self._subscribers: List[Observer] = []
        self._fileDb = FileDb()
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

    def publish_video(self) -> None:
        subs = self._fileDb.get_subscribers(self.get_name())
        for sub in subs:
            self.attach(sub)
        print(f"Notifying subscribers of {self.get_name()}")
        self.notify()
