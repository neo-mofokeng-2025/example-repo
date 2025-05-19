class Adult:
    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_colour = eye_color
        self.hair_colour = hair_color

    def can_drive(self):
        if age > 18:
            print(f"{self.name}, you are old enough to drive")


class Child(Adult):
    def __init__(self, name, age, eye_color, hair_color):
        super().__init__(name, age, eye_color, hair_color)
    
    def can_drive(self):
        print(f"{self.name}, you are too young to drive ")


def check_integer():
    try:
        age = int(input("Enter age\t"))
        return age
    except ValueError:
        print("You did not enter a number")
        check_integer()


while True:
    name = input("Enter name\t").title()
    age = check_integer()
    if age is None:
        print("Ooops an error happened",
              "Enter age again")
        age = check_integer()
    hair_color = input("Enter hair colour\t").title()
    eye_colour = input("Enter eye colour\t").title()

    if age > 18:
        adult = Adult(name, age, eye_colour, hair_color)
        adult.can_drive()
    else:
        child = Child(name, age, eye_colour, hair_color)
        child.can_drive()