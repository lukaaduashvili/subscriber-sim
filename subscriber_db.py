from abc import abstractmethod
from typing import List

from channel import Channel
from singleton import Singleton
from user import User


class DbInterface:
    @abstractmethod
    def subscribe_to_channel(self, user_name: str, channel_name: str) -> None:
        pass

    @abstractmethod
    def unsubscribe_from_channel(self, user_name: str, channel_name: str) -> None:
        pass

    @abstractmethod
    def get_subscribers(self, channel_name: str) -> List[User]:
        pass

    @abstractmethod
    def get_channels(self) -> List[Channel]:
        pass


class FileDb(DbInterface, metaclass=Singleton):
    _channels: List[Channel] = []

    _file: str = "text_db.txt"

    def get_channels(self) -> List[Channel]:
        return self._channels

    def subscribe_to_channel(self, user_name: str, channel_name: str) -> None:
        with open(self._file, "r+") as file:
            lines: List[str] = file.readlines()
            for line in lines:
                curr_user = line.strip().split(".")[1]
                curr_channel = line.strip().split(".")[0]
                if curr_channel == channel_name and curr_user == user_name:
                    return
            file.seek(0, 2)
            file.write("{}.{}\n".format(channel_name, user_name))
            
    def update_channel(self, channel_name) -> str:
        pass

    def unsubscribe_from_channel(self, user_name: str, channel_name: str) -> None:
        with open(self._file, "r+") as file:
            lines: List[str] = file.readlines()
            file.seek(0)
            for line in lines:
                curr_user = line.strip().split(".")[1]
                curr_channel = line.strip().split(".")[0]
                if curr_user != user_name or curr_channel != channel_name:
                    file.write(line)
                file.truncate()

    def get_subscribers(self, channel_name: str) -> List[User]:
        with open(self._file, "r") as file:
            lines: List[str] = file.readlines()
            users: List[User] = []
            for line in lines:
                curr_user = line.strip().split(".")[1]
                curr_channel = line.strip().split(".")[0]
                if curr_channel == channel_name:
                    curr_sub: User = User(curr_user)
                    users.append(curr_sub)
            return users
