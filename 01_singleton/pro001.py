class Singleton:
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
        return self.instance


s = Singleton()
print("Object created:", s)

s1 = Singleton()
print("Object created:", s1)
