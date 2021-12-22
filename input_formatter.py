from typing import List

from channel import Channel
from singleton import Singleton
import re
import subscriber_db


class InputFormatter(metaclass=Singleton):
    _fileDb = subscriber_db.FileDb()
    _pattern = "<.*?>"

    def run(self) -> None:
        while True:
            if not self._read_console_input():
                break

    def _read_console_input(self) -> bool:
        inp: str = input("Enter Exit to quit:")
        if inp == "Exit":
            return False
        self._process_console_input(inp)
        return True

    def _process_console_input(self, inpt: str) -> None:
        if re.match("subscribe", inpt):
            ss = re.findall(self._pattern, inpt)
            if len(ss) == 2:
                self._sub_to_channel(ss)
            else:
                print("Incorrect input")
        elif re.match("publish", inpt):
            ss = re.findall(self._pattern, inpt)
            if len(ss) == 1:
                name: str = ss[0][1:len(ss[0]) - 1]
                channel = Channel(name)
                channel.publish_video()
            else:
                print("Incorrect input")
        else:
            print("Incorrect input")

    def _sub_to_channel(self, ls: List[str]) -> None:
        user_name: str = ls[0][1:len(ls[0]) - 1]
        channel_name: str = ls[1][1:len(ls[1]) - 1]
        self._fileDb.subscribe_to_channel(user_name, channel_name)
