from pyforwarder import forwarder

def test_mainline():
    class Tail(object):
        def wag(self, speed=5):
            """Hello world"""
            if speed > 10:
                print("Wagging tail very happily")
            else:
                print("Wagging tail")

    @forwarder('_tail', target_class=Tail)
    class Dog(object):
        def __init__(self):
            self._tail = Tail()

    rover = Dog()
    rover.wag(speed=11)
