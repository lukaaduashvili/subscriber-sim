import io
import sys

from channel import Channel
from input_formatter import InputFormatter
from subscriber_db import FileDb

db: FileDb = FileDb()


def test_db() -> None:
    captured_output = io.StringIO()
    sys.stdout = captured_output

    db.subscribe_to_channel("John", "Alice")

    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "John subscribed to Alice\n"
    assert len(db.get_subscribers("Alice")) == 1

    db.subscribe_to_channel("John", "Alice")

    assert len(db.get_subscribers("Alice")) == 1

    db.unsubscribe_from_channel("John", "Alice")
    assert len(db.get_subscribers("Alice")) == 0


def test_publish() -> None:
    db.subscribe_to_channel("Petre", "Brinji")
    assert db.get_subscribers("Brinji")[0].get_name() == "Petre"

    channel: Channel = Channel("Brinji")
    captured_output = io.StringIO()
    sys.stdout = captured_output
    channel.publish_video()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Notifying subscribers of Brinji\nPetre\n"


def test_formatter() -> None:
    ipf: InputFormatter = InputFormatter()
    captured_output = io.StringIO()
    sys.stdout = captured_output
    ipf.process_console_input("Jibbersih")
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Incorrect input\n"

    ipf.process_console_input("subscribe <Erick> to <Emily>")
    assert len(db.get_subscribers("Emily")) == 1

    ipf2: InputFormatter = InputFormatter()
    captured_output2 = io.StringIO()
    sys.stdout = captured_output2
    ipf2.process_console_input("publish video on <Emily>")
    sys.stdout = sys.__stdout__
    assert captured_output2.getvalue() == "Notifying subscribers of Emily\nErick\n"
