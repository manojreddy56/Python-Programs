from datetime import date

class Person:
    def __init__(self, name, country, DOB):
        self.name = name
        self.country = country
        self.DOB = DOB
    
    def cal_age(self):
        today = date.today()
        age = today.year - self.DOB.year
        if today < date(today.year, self.DOB.month, self.DOB.day):
            age -= 1
        return age

person1 = Person("Manoj", "France", date(2003, 8, 27))
person2 = Person("Surya", "Canada", date(2002, 8, 9))
person3 = Person("John", "USA", date(2000, 1, 1))

print("name: ", person1.name, "Country: ", person1.country, "age: ", person1.cal_age())
print("name: ", person2.name, "Country: ", person2.country, "age: ", person2.cal_age())
print("name: ", person3.name, "Country: ", person3.country, "age: ", person3.cal_age())