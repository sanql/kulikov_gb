from itertools import count
from math import factorial

# def fact_gen():
#     for el in count(1):
#         yield factorial(el)
#
# generator = fact_gen()
# x = 0
#
# for i in generator:
#     if x == 15:
#         break
#     else:
#         x += 1
#         print(f"Factorial {x} = {i}")

#----------------------------------------------------------------------------

def fact_gen(number):
    f_num = 1
    if number == 0:
        yield f'{number}! = 1'
    for i in range(1, number + 1):
        f_num *= i
        yield f'{i}! = {f_num}'

for el in fact_gen(int(input('Factorial number: '))):
    print(el)

