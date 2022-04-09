class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_detail(self):
        return "name:" + self.name + ", age:" + str(self.age)
# 解释继承
class ElectricDog(Dog):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex
    def get_detail(self):
        return super().get_detail() + ", sex:" + self.sex

if __name__ == '__main__':
    dog = ElectricDog("a", 123, '男')
    print(dog.get_detail())