from subscriber_db import FileDb

if __name__ == '__main__':
    fileDb = FileDb()
    fileDb.subscribe_to_channel("luks", "Bendover Productions")
    fileDb.subscribe_to_channel("Lika", "Bendover Productions")
    fileDb.subscribe_to_channel("GGG", "Plus")
    # fileDb.unsubscribe_from_channel("luks", "Bendover Productions")

    subs = fileDb.get_subscribers("Bendover Productions")
    for sub in subs:
        print(sub.get_name())
