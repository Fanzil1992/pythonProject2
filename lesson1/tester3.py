# int_var = 500
# float_var = 50.9
# string_var_text = 'Hello world'
# string_var_num = '123.2'
# bool_var = True
#
#  # (int) - integer
#  # (float) - float
#  # (str) - string
#  # (bool) - boolen
#
# print(string_var_text+str(int_var))
# # Альтернативный вариант вышеуказанного кода
# print(string_var_text, int_var)
#
# print(type(int_var))
# print(string_var_text+str(float_var))
# print(string_var_text+str(bool_var))
#
# # Конвертация из целого дробное число
# print(int_var)
# print(float(int_var))
# # Конвертация из дробного целое число
# print(float_var)
# print(int(float_var))
#
# print(type(int(float(string_var_num))))
# print(int(float(string_var_num)))
#
# print(bool(int_var))
# user_input = input('please enter something:')
# print(type(user_input))
# user_input = float(user_input)
# print(user_input)

# пример
a = float(input('Side A: '))
b = float(input('Side B: '))
c = float(input('Side C: '))
# Периметр трегольника
half_p = (a+b+c)/2
print(half_p)
# Площадь треугольника
area = (half_p * (half_p - a) * (half_p-b) * (half_p-c)) ** 0.5
print(area)