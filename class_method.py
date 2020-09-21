


class Test:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Test({self.ingredients!r})'

    @classmethod
    def cappechino(cls):
        return cls(['cap', 'suger', 'water'])

    @classmethod
    def hazelnut(cls):
        return cls(['hazelnut', 'sugar', 'water']) 



Test.cappechino()
Test.hazelnut()       