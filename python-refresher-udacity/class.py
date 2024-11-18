class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.__person_age = age

    def birthday(self):
        self.__person_age += 1

    def getName(self):
        return self.person_name
    
    def getPersonAge(self):
        return self.__person_age
    
    
bob = Person('Bob', 32)
print(bob.getName())

bob.birthday()
print(bob.getPersonAge()) 
# prints Bob