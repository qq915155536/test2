stu1 = {
    'stu_school': 'oldboy',
    'name': 'dog',
    'age': 18,
    'gender': 'male'
}

stu2 = {
    'stu_school': 'oldboy',
    'name': 'cat',
    'age': 19,
    'gender': 'female'
}


class Student:
    stu_school = 'oldboy'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def choose_class(self):
        print('%s is choosing a course' %self.name)

if __name__ == '__main__':
    obj1 = Student('dog',18,'male')
    obj1.choose_class()
    print(type(obj1))
