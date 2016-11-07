
class Person:

    def __init__(self, initialAge):
        if initialAge < 0:
            print ("Age is not valid, setting age to 0.")
            age = 0
        else:
            age = initialAge
        self.age = age

    def amIOld(self):
        if self.age < 13:
            print ("You are young.")
        elif self.age < 18:
            print ("You are a teenager.")
        else:
            print ("You are old.")

    def yearPasses(self):
        self.age += 1