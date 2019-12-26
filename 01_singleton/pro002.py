class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called but nothing is created")
        else:
            print("instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = Singleton()
        return cls.__instance


# class initialized, but object not created
s = Singleton()
s1 = Singleton()

# This returns None although the object is initialized
print(s._Singleton__instance)
print(s1._Singleton__instance)

# We now explicitly initialize the object:
s.getInstance()
s1.getInstance()

# Which is now accessible
print(s._Singleton__instance)
print(s1._Singleton__instance)
