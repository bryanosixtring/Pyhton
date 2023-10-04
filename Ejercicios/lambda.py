#Lambda, funciones anonimas

lambda firts_value, second_value: firts_value+second_value

sum_two_values = lambda first_value, second_value: first_value+second_value
print(sum_two_values(2,4))

#lambda en una función

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))

""""

def sum_two_values(first_value, second_value): return first_value + second_value

print(sum_two_values(2,4))

def sum_three_values(value):
    return lambda firts_value, second_value: firts_value + second_value + value

print(sum_three_values(5(2,4)))

"""