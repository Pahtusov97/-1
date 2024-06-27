# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("1st program")
print(9 ** 0.5 * 5)
print(9 ** 0.5 * 5 == 15.0)

print("2st program")
print(9.99 > 9.98 and 1000 != 1001)
print(9.99 > 9.98 or 1001 != 1001)

print("3st program")
a = 1234 % 1000
b = a // 10
c = 5678 % 1000
d = c // 10
print(b + d == 90)

print("4st program")
a = int(13.42)
b = (42.13 * 100 % 100)
print(a == b)
# вроде все должно быть правильно в рамках задания! Не совсем понял как сюда приписать and и or
# типо (a >= b and a<=b) ; (a == b or b < a) и т.д.