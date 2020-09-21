from abc import abstractmethod, ABCMeta

class ABCBase(metaclass=ABCMeta):

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):    
        pass

class ChildAbc(ABCBase):

    def foo(self):
        print('cHild implemented Foo')        

    def bar(self):
        print('Child implemented Bar')

a =ChildAbc()
a.foo()
a.bar()
print(type(a))