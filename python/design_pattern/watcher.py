

class Watcher1(object):

    def __init__(self):
        self.event_type = "watch1"

    def notify(self):
        print("I am watch1")


class Watcher2(object):

    def __init__(self):
        self.event_type = "watch2"

    def notify(self):
        print("I am watch2")


class Publisher(object):
    def __init__(self):
        self.event_map = {}

    def bind(self, event_type, watcher):
        if event_type not in self.event_map:
            self.event_map[event_type] = []
        self.event_map[event_type].append(watcher)

    def unbind(self, event_type, watcher):
        if event_type in self.event_map:
            self.event_map[event_type].remove(watcher)

    def pub(self, event_type):
        watch_lst = self.event_map.get(event_type, [])
        for watcher in watch_lst:
            watcher.notify()


if __name__ == "__main__":
    publisher = Publisher()
    watch1 = Watcher1()
    watch2 = Watcher2()
    watch3 = Watcher2()
    publisher.bind("notify1", watch1)
    publisher.bind("notify2", watch2)
    publisher.bind("notify2", watch3)
    # publisher.pub("notify1")
    publisher.pub("notify2")

