class EuropeanSocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


class Socket(EuropeanSocketInterface):

    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


class USASocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass


class Adapter(USASocketInterface):
    _socket = None

    def __init__(self, socket):
        self._socket = socket

    def voltage(self):
        return 120

    def live(self):
        self._socket.live()

    def neutral(self):
        self._socket.neutral()


class ElectricKettle:
    _power = None

    def __init__(self, power):
        self._power = power

    def boil(self):
        if self._power.voltage() > 110:
            print("kettle is on fire")
        elif self._power.live() == 1 and \
                self._power.neutral() == -1:
            print("coffee time")
        else:
            print("no power")


def main():
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    kettle.boil()

    return 0


if __name__ == '__main__':
    main()

# NOTE: commonly called as mapper in dev community
# NOTE: interface implementation and encapsulation plays a pivotal role

