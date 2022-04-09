"""
用于学习函数的py文件
"""
def describe_pet(animal_type, pet_name = 'tom'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "`s name is " + pet_name.title() + "!")
    return pet_name.title()

describe_pet('dog')
describe_pet('dog', 'jerry')
describe_pet(animal_type='dog')
describe_pet(animal_type='dog', pet_name='tom')
pet = describe_pet(pet_name='tom', animal_type='dog')
print("pet name:" + pet)


def build_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


profile = build_profile('zhao', 'yong', age=18, sex='男')
print(profile)

def make_pizza(size, *toppings):
    rst = []
    rst.append(size)
    for topping in toppings:
        rst.append(topping)
    return rst;


print(make_pizza("a", 14, 35))
