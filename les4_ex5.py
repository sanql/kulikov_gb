

from functools import reduce

def mul_list(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(100, 1001, 2)]
print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(mul_list, uniq_list)}")



print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))