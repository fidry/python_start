def say_hi(name: str | None = None):
    if name:
        print(f'Hello, {name}!!')
    else:
        print(f'Hello!!')


def my_sum(
        a: int | float,
        b: int | float = 0,
):
    print(a + b)


def get_smallest_number(a: int | float, b: int | float) -> int | float:
    if a < b:
        return a
    return b


def foo(a: int) -> int:
    return a ** 2


print(get_smallest_number(-5, -432))


# q = 5
# q = foo(a=q)
# print(q)
# print(foo(a=q))
# print(foo(a=2))
# print(foo(a=15))
# print(foo(a=16))
# res = foo(a=q)

# say_hi('Bob')
# say_hi(name='John')
# say_hi()

# get_smallest_number(3, b=9)  # 3
# get_smallest_number(-4, 32.54)  # -4


# a = int(input('введите число: '))
# b = int(input('введите число: '))
# my_sum(2, 3)
# my_sum(5, 5)
# my_sum(7, 10)
# my_sum(9, 0)
# # my_sum(int(input('введите число: ')), int(input('введите число: ')))
# my_sum(a=9, b=10)
# my_sum(b=9, a=100)
#
# my_sum(a=9.5, b=1)
