#绝对值
print("abs(-10) : " + str(abs(-10)) + "\n")

#遍历下标和元素
print("In ['first','second','third']")
for i, num in enumerate(["first", "second", "third"]):
    print(i, num)
print()

#判断类型
print("isinstance('str',str) : " + str(isinstance("str", str)))
print("isinstance(5.5,int) : " + str(isinstance(5.5, int)) + "\n")

#得到类型
print("type(False) : " + str(type(False)))
print("type(5.5) : " + str(type(5.5)) + "\n")

#获取长度
print("len('Hello World!') : " + str(len('Hello World!')))
print("len([1,2,3,4,5]) : " + str(len([1, 2, 3, 4, 5])) + "\n")

#排序
print("sorted([3,4,2,1,5]) : " + str(sorted([3, 4, 2, 1, 5])) + "\n")

#求和
print("sum((1,2,3,4,5,6)) : " + str(sum((1, 2, 3, 4, 5, 6))))
print("sum([[1,2],[3,4],[5,6]],[]) : " +
      str(sum([[1, 2], [3, 4], [5, 6]], [])) + "\n")

#聚合每个可迭代对象的元素
zip1 = ['1', '2', '3']
zip2 = ['4', '5', '6']
for i in zip(zip1, zip2):
    print(i)
print()

#转二进制
print("bin(14) : " + bin(14))
print("f'{14:b}' : " + f'{14:b}' + "\n")

#迭代
iter_list = [1, 2, 3, 4, 5]
iter_element = iter(iter_list)
print("iter the list[1,2,3,4,5]:")
while True:
    try:
        print(next(iter_element))
    except BaseException:
        break

#判断True False
print(bool(None))
print(bool([1, 2, 3]))

#转为bytes
print(bytes('string', encoding="utf-8"))
print(bytes('我是中文', encoding="utf-8"))

#筛选
def number_odd(a):
    if a % 2 == 0:
        return True
    else:
        return False


print(list(filter(number_odd, [1, 6, 9, 8])))

#批量处理
def number_pow(a):
    return a**2

print(list(map(number_pow, [1, 2, 3, 4])))

#四舍五入
print(round(1.4))
print(round(3.7))

#取绝对值
print(abs(-10))

#都为True则返回True
lst=[0,1,2]
print(all(lst))

#如何一个为True则返回True
lst=["", 0, ""]
print(any(lst))

#得到整除和取余的结果
print(divmod(5,3))

#花式打印
print("a", "b", sep="", end="\nend\n")
print("a", "b", sep="\t", end=" end\n")
asc = "你好"
print(f"ascii : {asc!a}")
print(f"repr : {asc!r}")
print(f"str : {asc!s}")
dct = {"John":98, "Alice":89, "Steven":95}
for i,j in dct.items():
	print(f"{i:10} : {j:10d}")
