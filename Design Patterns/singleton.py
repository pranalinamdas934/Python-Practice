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
