if __name__ == '__main__':
    print("123".title());
    print(0.2 + 0.1)
    # zhaoyong08
    age = 23
    a = ["a", "b", "c"]
    print(a[1])
    print(a[-2])
    # 修改元素
    a[1] = 'd'
    # 结尾增加元素
    a.append('e')
    # 某些位置插入元素
    a.insert(1, 'f')
    # 删除元素
    del a[0]
    # 弹出
    pop = a.pop()
    # 根据值进行删除
    a.remove('d')
    # 临时排序
    sorted(a, reverse=True);
    # 永久排序
    a.sort(reverse=True)
    # 反转列表
    a.reverse()
    # 获取长度
    i = len(a)

    # 操作数据
    cats = ["zhaoyong", "davied", "zhangsan"]
    for cat in cats:
        print(cat)
    for value in range(1, 5):
        print(value)
    # 自定义步长
    numbers = list(range(2, 11, 2))
    for number in numbers:
        print(number)
    min(numbers)
    max(numbers)
    sum(numbers)
    # 列表解析
    squares = [value ** 2 for value in range(1, 11)]
    print(squares)
    # 切片
    print(squares[0:3])
    for square in squares[-3:]:
        print(square)
    # 复制列表 如果直接等于 相当于指向了相同的 数组
    squares_copy = squares[:]
    # 元组是指元素都不可变的数组 修改会报错
    dimensions = (200, 50)
    print(dimensions[0])
    print(dimensions[1])
    # 但是变量可以重新赋值
    dimensions = (300, 400)

    cat = 'zhaOYONG'
    print(cat.lower())
    print(cat)

    test = ['a', 'b', 'c', 'd']
    result = 'a' not in test
    print(result)
    if 'w' in test:
        print('w')
    elif 'e' in test:
        print('e')
    else:
        print('m')
    # 判断列表是否为空
    if test:
        for te in test:
            print(te)
    else:
        print("列表为空")

    dict_zhao = {}
    dict_zhao['name'] = 'zhaoyong'
    dict_zhao['age'] = 18
    dict_zhao['color'] = ['red', 'yellow', 'black']
    dict_zhao['book'] = {'a':'a'}
    dict_zhao['age'] = 28
    for key, value in dict_zhao.items():
        print(key)
        print(value)
    del dict_zhao['age']
    for key in dict_zhao.keys():
        print(key)
    for value in dict_zhao.values():
        print(value)

    name = input("Please enter your name:")
    print("Hello, " + name + "!")
    age = input("your age:")
    print("your age:" + str(int(age) + 1))
    test = ''
    while True:
        if test == 'zhaoyong':
            print('zhaoyong')
            break
        if test == 'zhaoyong08':
            continue
        test = 'zhaoyong'