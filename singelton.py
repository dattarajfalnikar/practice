#/usr/bin/lib/python3
class Singleton:
    __instance = None

    class _Singleton:

        def __init__(self):
            self.value = 'Test'
            
    def __new__(cls):
        if not Singleton.__instance:
            Singleton.__instance = Singleton._Singleton()   
            print('Inside New Singleton')
        return Singleton.__instance

s = Singleton()
s1 =Singleton()
s2 = Singleton()

print('s-{} s1-{} s2-{}'.format(s, s1, s2))


class Singleton:
    __instance = None
           
    def __init__(self):
        if not Singleton.__instance:
            Singleton.__instance = self
            print('Inside New Singleton')
        else:
            raise Exception("This is Singleton")

s = Singleton()
s1 =Singleton()
s2 = Singleton()

print('s-{} s1-{} s2-{}'.format(s, s1, s2))