class MySingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if MySingleton._instance is None:
            MySingleton._instance = MySingleton()
        return MySingleton._instance

    def __init__(self):
        if MySingleton._instance is not None:
            raise Exception("can not create another instance")
        MySingleton._instance = self


x = MySingleton()
y = MySingleton.get_instance()
z = MySingleton.get_instance()

print(x)
print(y)
print(z)

# NOTE: Logger classes are examples of singleton pattern
# NOTE: in the cloud design pattern world we would need a persistent storage to achieve this
# explore if we can make it thread safe


import threading


class EventBus(object):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if EventBus._instance is None:
            with EventBus._lock:
                if EventBus._instance is None:
                    EventBus._instance = super(EventBus, cls).__new__(cls)
        return EventBus._instance

    def __init__(self):
        self.clients = []
