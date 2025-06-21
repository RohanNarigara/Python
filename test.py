class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, language, salary):
        self.language = language
        self.salary = salary
        print("I am running")

harry = Employee("JavaScript", 1300000)
print(harry.language, harry.salary)