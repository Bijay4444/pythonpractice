class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def shit(self):
        print("shit")


class Cat(Mammal):
    def piss(self):
        print("piss")


dog1= Dog()
dog1.walk()
dog1.shit()
cat1= Cat()
cat1.walk()
cat1.piss()