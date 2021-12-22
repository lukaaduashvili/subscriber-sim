from observer_interfaces import Observer, Subject


class User(Observer):

    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def update(self, subject: Subject) -> None:
        print(self.get_name())
